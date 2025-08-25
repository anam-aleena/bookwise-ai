import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD, NMF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.sparse import csr_matrix
import warnings
warnings.filterwarnings('ignore')

class AdvancedBookRecommendationSystem:
    """
    Advanced book recommendation system implementing multiple ML algorithms:
    - Smart Popularity Based
    - Collaborative Filtering (SVD)
    - Content-Based Filtering (TF-IDF)
    - Cluster-Based Filtering
    - Matrix Factorization (NMF)
    - Hybrid Ensemble
    """
    
    def __init__(self):
        from data_generator import generate_book_data
        
        # Generate dataset
        self.books_df, self.users_df, self.ratings_df = generate_book_data()
        
        # Initialize components
        self._prepare_matrices()
        self._fit_collaborative_filtering()
        self._fit_content_based()
        self._fit_clustering()
        self._fit_matrix_factorization()
        
        # Set algorithm weights for hybrid approach
        self.algorithm_weights = {
            'smart_popularity': 0.15,
            'collaborative': 0.25,
            'content': 0.20,
            'cluster': 0.15,
            'matrix_factorization': 0.25
        }
    
    def _prepare_matrices(self):
        """Prepare user-item matrices and other data structures"""
        # Create user-item rating matrix
        self.ratings_pivot = self.ratings_df.pivot(
            index='user_id', 
            columns='book_id', 
            values='rating'
        ).fillna(0)
        
        # Create sparse matrix for memory efficiency
        self.sparse_matrix = csr_matrix(self.ratings_pivot.values)
        
        # Book popularity metrics
        book_stats = self.ratings_df.groupby('book_id').agg({
            'rating': ['mean', 'count']
        }).round(2)
        book_stats.columns = ['avg_rating', 'rating_count']
        
        # Smart popularity score (weighted by both rating and frequency)
        book_stats['popularity_score'] = (
            book_stats['avg_rating'] * np.log1p(book_stats['rating_count'])
        )
        
        self.book_popularity = book_stats.sort_values('popularity_score', ascending=False)
    
    def _fit_collaborative_filtering(self):
        """Fit SVD-based collaborative filtering model"""
        # Use TruncatedSVD for dimensionality reduction
        self.svd_model = TruncatedSVD(n_components=100, random_state=42)
        self.user_factors = self.svd_model.fit_transform(self.sparse_matrix)
        self.item_factors = self.svd_model.components_.T
        
        # Compute user similarity matrix
        user_similarity = cosine_similarity(self.user_factors)
        self.user_similarity_df = pd.DataFrame(
            user_similarity,
            index=self.ratings_pivot.index,
            columns=self.ratings_pivot.index
        )
    
    def _fit_content_based(self):
        """Fit TF-IDF based content filtering model"""
        # Create feature text combining multiple attributes
        self.books_df['features'] = (
            self.books_df['genre'] + ' ' + 
            self.books_df['author'] + ' ' + 
            self.books_df['title']
        )
        
        # Apply TF-IDF vectorization with bi-gram support
        self.tfidf_vectorizer = TfidfVectorizer(
            stop_words='english',
            ngram_range=(1, 2),
            max_features=5000
        )
        
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.books_df['features'])
        
        # Compute book similarity matrix
        self.book_similarity = cosine_similarity(self.tfidf_matrix)
        self.book_similarity_df = pd.DataFrame(
            self.book_similarity,
            index=self.books_df['book_id'],
            columns=self.books_df['book_id']
        )
    
    def _fit_clustering(self):
        """Fit K-means clustering for users and books"""
        # User clustering based on rating patterns
        user_features = self.ratings_pivot.fillna(0)
        scaler = StandardScaler()
        scaled_user_features = scaler.fit_transform(user_features)
        
        self.user_kmeans = KMeans(n_clusters=5, random_state=42)
        self.user_clusters = self.user_kmeans.fit_predict(scaled_user_features)
        
        # Book clustering based on features
        book_features = self.books_df[['publication_year', 'pages']].fillna(0)
        # Add encoded genre features
        genre_encoded = pd.get_dummies(self.books_df['genre'])
        book_features = pd.concat([book_features, genre_encoded], axis=1)
        
        scaled_book_features = scaler.fit_transform(book_features)
        
        self.book_kmeans = KMeans(n_clusters=8, random_state=42)
        self.book_clusters = self.book_kmeans.fit_predict(scaled_book_features)
    
    def _fit_matrix_factorization(self):
        """Fit Non-negative Matrix Factorization model"""
        self.nmf_model = NMF(n_components=50, random_state=42, max_iter=1000)
        self.user_factors_nmf = self.nmf_model.fit_transform(self.ratings_pivot.fillna(0))
        self.item_factors_nmf = self.nmf_model.components_.T
    
    def smart_popularity_recommendations(self, user_id, n_recommendations=10):
        """Generate recommendations based on smart popularity algorithm"""
        # Get books already rated by user
        user_books = set(self.ratings_df[self.ratings_df['user_id'] == user_id]['book_id'])
        
        # Get user's preferred genres
        if user_books:
            user_genres = self.books_df[
                self.books_df['book_id'].isin(user_books)
            ]['genre'].value_counts()
            preferred_genre = user_genres.index[0] if len(user_genres) > 0 else None
        else:
            preferred_genre = None
        
        # Filter out already rated books
        available_books = self.book_popularity[
            ~self.book_popularity.index.isin(user_books)
        ].copy()
        
        # Boost recommendations from preferred genre
        if preferred_genre:
            genre_books = self.books_df[self.books_df['genre'] == preferred_genre]['book_id']
            available_books.loc[
                available_books.index.isin(genre_books), 'popularity_score'
            ] *= 1.2
        
        # Get top recommendations
        top_book_ids = available_books.head(n_recommendations).index.tolist()
        
        return self.books_df[self.books_df['book_id'].isin(top_book_ids)]
    
    def collaborative_filtering_recommendations(self, user_id, n_recommendations=10):
        """Generate recommendations using collaborative filtering"""
        if user_id not in self.user_similarity_df.index:
            return self.smart_popularity_recommendations(user_id, n_recommendations)
        
        # Get similar users
        similar_users = self.user_similarity_df[user_id].sort_values(ascending=False)[1:11]
        
        # Get books rated by similar users
        user_books = set(self.ratings_df[self.ratings_df['user_id'] == user_id]['book_id'])
        
        recommendations = {}
        for similar_user, similarity in similar_users.items():
            similar_user_books = self.ratings_df[
                (self.ratings_df['user_id'] == similar_user) & 
                (self.ratings_df['rating'] >= 4.0)
            ]
            
            for _, row in similar_user_books.iterrows():
                if row['book_id'] not in user_books:
                    if row['book_id'] not in recommendations:
                        recommendations[row['book_id']] = 0
                    recommendations[row['book_id']] += similarity * row['rating']
        
        # Sort by predicted rating
        sorted_recommendations = sorted(
            recommendations.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:n_recommendations]
        
        recommended_book_ids = [book_id for book_id, _ in sorted_recommendations]
        
        if not recommended_book_ids:
            return self.smart_popularity_recommendations(user_id, n_recommendations)
        
        return self.books_df[self.books_df['book_id'].isin(recommended_book_ids)]
    
    def content_based_recommendations(self, user_id, n_recommendations=10):
        """Generate recommendations using content-based filtering"""
        # Get user's reading history
        user_books = self.ratings_df[
            (self.ratings_df['user_id'] == user_id) & 
            (self.ratings_df['rating'] >= 4.0)
        ]['book_id'].tolist()
        
        if not user_books:
            return self.smart_popularity_recommendations(user_id, n_recommendations)
        
        # Calculate content similarity scores
        similarity_scores = {}
        
        for user_book in user_books:
            if user_book in self.book_similarity_df.index:
                similar_books = self.book_similarity_df[user_book].sort_values(ascending=False)[1:21]
                
                for book_id, similarity in similar_books.items():
                    if book_id not in user_books:
                        if book_id not in similarity_scores:
                            similarity_scores[book_id] = 0
                        similarity_scores[book_id] += similarity
        
        # Sort by similarity score
        sorted_books = sorted(
            similarity_scores.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:n_recommendations]
        
        recommended_book_ids = [book_id for book_id, _ in sorted_books]
        
        if not recommended_book_ids:
            return self.smart_popularity_recommendations(user_id, n_recommendations)
        
        return self.books_df[self.books_df['book_id'].isin(recommended_book_ids)]
    
    def cluster_based_recommendations(self, user_id, n_recommendations=10):
        """Generate recommendations using cluster-based filtering"""
        if user_id > len(self.user_clusters):
            return self.smart_popularity_recommendations(user_id, n_recommendations)
        
        # Get user's cluster
        user_cluster = self.user_clusters[user_id - 1]
        
        # Get users in the same cluster
        cluster_users = [
            i + 1 for i, cluster in enumerate(self.user_clusters) 
            if cluster == user_cluster and i + 1 != user_id
        ]
        
        # Get books already rated by the user
        user_books = set(self.ratings_df[self.ratings_df['user_id'] == user_id]['book_id'])
        
        # Find popular books in the cluster
        cluster_ratings = self.ratings_df[
            (self.ratings_df['user_id'].isin(cluster_users)) &
            (self.ratings_df['rating'] >= 4.0)
        ]
        
        if cluster_ratings.empty:
            return self.smart_popularity_recommendations(user_id, n_recommendations)
        
        cluster_book_scores = cluster_ratings.groupby('book_id').agg({
            'rating': ['mean', 'count']
        })
        cluster_book_scores.columns = ['avg_rating', 'count']
        cluster_book_scores['score'] = (
            cluster_book_scores['avg_rating'] * np.log1p(cluster_book_scores['count'])
        )
        
        # Filter out already rated books
        available_books = cluster_book_scores[
            ~cluster_book_scores.index.isin(user_books)
        ].sort_values('score', ascending=False)
        
        recommended_book_ids = available_books.head(n_recommendations).index.tolist()
        
        if not recommended_book_ids:
            return self.smart_popularity_recommendations(user_id, n_recommendations)
        
        return self.books_df[self.books_df['book_id'].isin(recommended_book_ids)]
    
    def matrix_factorization_recommendations(self, user_id, n_recommendations=10):
        """Generate recommendations using matrix factorization"""
        if user_id > len(self.user_factors_nmf):
            return self.smart_popularity_recommendations(user_id, n_recommendations)
        
        # Get user factor vector
        user_vector = self.user_factors_nmf[user_id - 1]
        
        # Compute predicted ratings
        predicted_ratings = np.dot(user_vector, self.item_factors_nmf.T)
        
        # Get books already rated by user
        user_books = set(self.ratings_df[self.ratings_df['user_id'] == user_id]['book_id'])
        
        # Create recommendations dataframe
        recommendations_df = pd.DataFrame({
            'book_id': range(1, len(predicted_ratings) + 1),
            'predicted_rating': predicted_ratings
        })
        
        # Filter out already rated books
        recommendations_df = recommendations_df[
            ~recommendations_df['book_id'].isin(user_books)
        ].sort_values('predicted_rating', ascending=False)
        
        recommended_book_ids = recommendations_df.head(n_recommendations)['book_id'].tolist()
        
        return self.books_df[self.books_df['book_id'].isin(recommended_book_ids)]
    
    def hybrid_recommendations(self, user_id, n_recommendations=10):
        """Generate recommendations using hybrid ensemble approach"""
        # Get recommendations from all algorithms
        algorithms = {
            'smart_popularity': self.smart_popularity_recommendations,
            'collaborative': self.collaborative_filtering_recommendations,
            'content': self.content_based_recommendations,
            'cluster': self.cluster_based_recommendations,
            'matrix_factorization': self.matrix_factorization_recommendations
        }
        
        # Get recommendations from each algorithm
        all_recommendations = {}
        for algo_name, algo_func in algorithms.items():
            try:
                recs = algo_func(user_id, n_recommendations * 2)
                weight = self.algorithm_weights[algo_name]
                
                for idx, (_, book) in enumerate(recs.iterrows()):
                    book_id = book['book_id']
                    # Score decreases with rank, weighted by algorithm weight
                    score = weight * (1.0 / (idx + 1))
                    
                    if book_id not in all_recommendations:
                        all_recommendations[book_id] = 0
                    all_recommendations[book_id] += score
            except Exception:
                continue
        
        # Sort by combined score
        sorted_recommendations = sorted(
            all_recommendations.items(),
            key=lambda x: x[1],
            reverse=True
        )[:n_recommendations]
        
        recommended_book_ids = [book_id for book_id, _ in sorted_recommendations]
        
        if not recommended_book_ids:
            return self.smart_popularity_recommendations(user_id, n_recommendations)
        
        return self.books_df[self.books_df['book_id'].isin(recommended_book_ids)]
    
    def get_user_reading_history(self, user_id):
        """Get user's reading history with book details"""
        user_ratings = self.ratings_df[self.ratings_df['user_id'] == user_id]
        
        if user_ratings.empty:
            return pd.DataFrame()
        
        # Merge with book details
        history = user_ratings.merge(self.books_df, on='book_id')
        return history.sort_values('rating', ascending=False)
    
    def evaluate_recommendations(self, user_id, algorithm='hybrid', n_recommendations=10):
        """Evaluate recommendation quality for a specific user"""
        # Get user's high-rated books (ground truth)
        high_rated_books = set(self.ratings_df[
            (self.ratings_df['user_id'] == user_id) & 
            (self.ratings_df['rating'] >= 4.0)
        ]['book_id'])
        
        # Get recommendations
        if algorithm == 'hybrid':
            recommendations = self.hybrid_recommendations(user_id, n_recommendations)
        else:
            algo_map = {
                'popularity': self.smart_popularity_recommendations,
                'collaborative': self.collaborative_filtering_recommendations,
                'content': self.content_based_recommendations,
                'cluster': self.cluster_based_recommendations,
                'matrix_factorization': self.matrix_factorization_recommendations
            }
            recommendations = algo_map[algorithm](user_id, n_recommendations)
        
        recommended_books = set(recommendations['book_id'])
        
        # Calculate metrics
        if not high_rated_books:
            return {'precision': 0, 'recall': 0, 'coverage': len(recommended_books) / len(self.books_df)}
        
        intersection = recommended_books.intersection(high_rated_books)
        
        precision = len(intersection) / len(recommended_books) if recommended_books else 0
        recall = len(intersection) / len(high_rated_books) if high_rated_books else 0
        coverage = len(recommended_books) / len(self.books_df)
        
        return {
            'precision': precision,
            'recall': recall,
            'coverage': coverage,
            'f1_score': 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        }
