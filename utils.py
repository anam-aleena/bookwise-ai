import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_sparsity(ratings_df, users_df, books_df):
    """Calculate the sparsity of the ratings matrix"""
    total_possible_ratings = len(users_df) * len(books_df)
    actual_ratings = len(ratings_df)
    sparsity = (1 - actual_ratings / total_possible_ratings) * 100
    return sparsity

def evaluate_recommendation_system(rec_system, test_users=None, n_recommendations=10):
    """
    Comprehensive evaluation of the recommendation system
    """
    if test_users is None:
        test_users = range(1, min(51, len(rec_system.users_df) + 1))  # Test first 50 users
    
    algorithms = ['hybrid', 'popularity', 'collaborative', 'content', 'cluster', 'matrix_factorization']
    
    results = {}
    
    for algorithm in algorithms:
        precision_scores = []
        recall_scores = []
        coverage_scores = []
        f1_scores = []
        
        for user_id in test_users:
            try:
                metrics = rec_system.evaluate_recommendations(
                    user_id, algorithm, n_recommendations
                )
                precision_scores.append(metrics['precision'])
                recall_scores.append(metrics['recall'])
                coverage_scores.append(metrics['coverage'])
                f1_scores.append(metrics['f1_score'])
            except Exception:
                continue
        
        if precision_scores:  # Only calculate if we have valid scores
            results[algorithm] = {
                'avg_precision': np.mean(precision_scores),
                'avg_recall': np.mean(recall_scores),
                'avg_coverage': np.mean(coverage_scores),
                'avg_f1_score': np.mean(f1_scores),
                'std_precision': np.std(precision_scores),
                'std_recall': np.std(recall_scores),
                'std_coverage': np.std(coverage_scores),
                'std_f1_score': np.std(f1_scores)
            }
    
    return results

def calculate_diversity(recommendations_df, books_df):
    """Calculate the diversity of recommendations based on genres"""
    if recommendations_df.empty:
        return 0
    
    # Get genres of recommended books
    rec_genres = books_df[books_df['book_id'].isin(recommendations_df['book_id'])]['genre']
    
    if len(rec_genres) == 0:
        return 0
    
    # Calculate entropy as diversity measure
    genre_counts = rec_genres.value_counts()
    genre_probs = genre_counts / len(rec_genres)
    diversity = -sum(p * np.log2(p) for p in genre_probs if p > 0)
    
    return diversity

def calculate_novelty(recommendations_df, popularity_scores):
    """Calculate novelty based on inverse popularity"""
    if recommendations_df.empty:
        return 0
    
    recommended_books = recommendations_df['book_id'].tolist()
    novelty_scores = []
    
    for book_id in recommended_books:
        if book_id in popularity_scores.index:
            # Higher novelty for less popular books
            novelty = 1 / (1 + popularity_scores.loc[book_id, 'popularity_score'])
            novelty_scores.append(novelty)
    
    return np.mean(novelty_scores) if novelty_scores else 0

def plot_algorithm_comparison(evaluation_results):
    """Create visualization comparing algorithm performance"""
    if not evaluation_results:
        return None
    
    algorithms = list(evaluation_results.keys())
    metrics = ['avg_precision', 'avg_recall', 'avg_coverage', 'avg_f1_score']
    
    data = []
    for algo in algorithms:
        for metric in metrics:
            data.append({
                'Algorithm': algo,
                'Metric': metric.replace('avg_', '').title(),
                'Score': evaluation_results[algo][metric]
            })
    
    results_df = pd.DataFrame(data)
    
    plt.figure(figsize=(12, 8))
    sns.barplot(data=results_df, x='Algorithm', y='Score', hue='Metric')
    plt.title('Algorithm Performance Comparison')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return plt.gcf()

def generate_user_profile_summary(rec_system, user_id):
    """Generate a comprehensive summary of a user's profile"""
    # Get user's rating history
    user_ratings = rec_system.ratings_df[rec_system.ratings_df['user_id'] == user_id]
    
    if user_ratings.empty:
        return {
            'total_ratings': 0,
            'avg_rating': 0,
            'favorite_genres': [],
            'reading_diversity': 0,
            'activity_level': 'inactive'
        }
    
    # Merge with book information
    user_books = user_ratings.merge(rec_system.books_df, on='book_id')
    
    # Calculate statistics
    total_ratings = len(user_ratings)
    avg_rating = user_ratings['rating'].mean()
    
    # Favorite genres
    genre_counts = user_books['genre'].value_counts()
    favorite_genres = genre_counts.head(3).index.tolist()
    
    # Reading diversity (entropy of genres)
    genre_probs = genre_counts / len(user_books)
    diversity = -sum(p * np.log2(p) for p in genre_probs if p > 0) if len(genre_probs) > 1 else 0
    
    # Activity level
    if total_ratings < 10:
        activity_level = 'low'
    elif total_ratings < 25:
        activity_level = 'medium'
    else:
        activity_level = 'high'
    
    return {
        'total_ratings': total_ratings,
        'avg_rating': round(avg_rating, 2),
        'favorite_genres': favorite_genres,
        'reading_diversity': round(diversity, 2),
        'activity_level': activity_level
    }

def calculate_coverage_metrics(rec_system, algorithm='hybrid', n_users=100):
    """Calculate various coverage metrics for the recommendation system"""
    # Book coverage - percentage of books that get recommended
    recommended_books = set()
    
    test_users = range(1, min(n_users + 1, len(rec_system.users_df) + 1))
    
    for user_id in test_users:
        try:
            if algorithm == 'hybrid':
                recs = rec_system.hybrid_recommendations(user_id, 10)
            else:
                # Add other algorithms as needed
                recs = rec_system.smart_popularity_recommendations(user_id, 10)
            
            recommended_books.update(recs['book_id'].tolist())
        except Exception:
            continue
    
    book_coverage = len(recommended_books) / len(rec_system.books_df)
    
    # User coverage - percentage of users who receive recommendations
    users_with_recs = 0
    for user_id in test_users:
        try:
            if algorithm == 'hybrid':
                recs = rec_system.hybrid_recommendations(user_id, 10)
            else:
                recs = rec_system.smart_popularity_recommendations(user_id, 10)
            
            if not recs.empty:
                users_with_recs += 1
        except Exception:
            continue
    
    user_coverage = users_with_recs / len(test_users)
    
    return {
        'book_coverage': book_coverage,
        'user_coverage': user_coverage,
        'books_recommended': len(recommended_books),
        'total_books': len(rec_system.books_df)
    }

def format_evaluation_report(evaluation_results):
    """Format evaluation results into a readable report"""
    if not evaluation_results:
        return "No evaluation results available."
    
    report = "Recommendation System Evaluation Report\n"
    report += "=" * 50 + "\n\n"
    
    # Sort algorithms by F1 score
    sorted_algos = sorted(
        evaluation_results.items(),
        key=lambda x: x[1]['avg_f1_score'],
        reverse=True
    )
    
    for i, (algorithm, metrics) in enumerate(sorted_algos, 1):
        report += f"{i}. {algorithm.upper()} ALGORITHM\n"
        report += "-" * 30 + "\n"
        report += f"Precision: {metrics['avg_precision']:.3f} (±{metrics['std_precision']:.3f})\n"
        report += f"Recall:    {metrics['avg_recall']:.3f} (±{metrics['std_recall']:.3f})\n"
        report += f"F1-Score:  {metrics['avg_f1_score']:.3f} (±{metrics['std_f1_score']:.3f})\n"
        report += f"Coverage:  {metrics['avg_coverage']:.3f} (±{metrics['std_coverage']:.3f})\n\n"
    
    return report

def export_recommendations_to_csv(rec_system, user_id, algorithm='hybrid', filename=None):
    """Export recommendations for a user to CSV file"""
    if algorithm == 'hybrid':
        recommendations = rec_system.hybrid_recommendations(user_id, 20)
    else:
        recommendations = rec_system.smart_popularity_recommendations(user_id, 20)
    
    if filename is None:
        filename = f"recommendations_user_{user_id}_{algorithm}.csv"
    
    recommendations.to_csv(filename, index=False)
    return filename

def get_system_statistics(rec_system):
    """Get comprehensive system statistics"""
    stats = {
        'total_books': len(rec_system.books_df),
        'total_users': len(rec_system.users_df),
        'total_ratings': len(rec_system.ratings_df),
        'sparsity': calculate_sparsity(rec_system.ratings_df, rec_system.users_df, rec_system.books_df),
        'avg_ratings_per_user': rec_system.ratings_df.groupby('user_id').size().mean(),
        'avg_ratings_per_book': rec_system.ratings_df.groupby('book_id').size().mean(),
        'genre_distribution': rec_system.books_df['genre'].value_counts().to_dict(),
        'rating_distribution': rec_system.ratings_df['rating'].round().value_counts().sort_index().to_dict(),
        'most_popular_books': rec_system.book_popularity.head(5).index.tolist(),
        'publication_year_range': (
            rec_system.books_df['publication_year'].min(),
            rec_system.books_df['publication_year'].max()
        )
    }
    
    return stats
