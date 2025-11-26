import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from books_database import BOOKS_DATABASE

def generate_book_data():
    """
    Generate realistic book recommendation dataset with:
    - 100 books across multiple genres with summaries and read links
    - 500 users with varying preferences
    - 6,299 ratings with 87.4% sparsity
    """
    
    np.random.seed(42)
    random.seed(42)
    
    books_data = []
    for book_id, book_info in BOOKS_DATABASE.items():
        books_data.append({
            'book_id': book_id,
            'title': book_info['title'],
            'author': book_info['author'],
            'genre': book_info['genre'],
            'publication_year': book_info['year'],
            'pages': book_info['pages'],
            'summary': book_info['summary'],
            'read_link': book_info['read_link'],
            'cover_color': book_info['cover_color']
        })
    
    books_df = pd.DataFrame(books_data)
    
    genres = list(set(book['genre'] for book in BOOKS_DATABASE.values()))
    
    users_data = []
    for user_id in range(1, 501):
        num_preferred_genres = random.choices([1, 2, 3], weights=[0.4, 0.4, 0.2])[0]
        preferred_genres = random.sample(genres, min(num_preferred_genres, len(genres)))
        
        activity_level = random.choices(['low', 'medium', 'high'], weights=[0.3, 0.5, 0.2])[0]
        
        users_data.append({
            'user_id': user_id,
            'preferred_genres': ','.join(preferred_genres),
            'activity_level': activity_level
        })
    
    users_df = pd.DataFrame(users_data)
    
    ratings_data = []
    target_ratings = 6299
    
    for user_id in range(1, 501):
        user_info = users_df[users_df['user_id'] == user_id].iloc[0]
        preferred_genres = user_info['preferred_genres'].split(',')
        activity_level = user_info['activity_level']
        
        if activity_level == 'low':
            num_ratings = random.randint(5, 15)
        elif activity_level == 'medium':
            num_ratings = random.randint(10, 25)
        else:
            num_ratings = random.randint(20, 40)
        
        if len(ratings_data) >= target_ratings:
            break
            
        remaining_ratings = target_ratings - len(ratings_data)
        num_ratings = min(num_ratings, remaining_ratings)
        
        available_books = books_df.copy()
        
        genre_weights = []
        for _, book in available_books.iterrows():
            if book['genre'] in preferred_genres:
                weight = 3.0
            else:
                weight = 1.0
            genre_weights.append(weight)
        
        if num_ratings > 0 and len(available_books) > 0:
            num_ratings = min(num_ratings, len(available_books))
            rated_books = np.random.choice(
                available_books.index,
                size=num_ratings,
                replace=False,
                p=np.array(genre_weights) / sum(genre_weights)
            )
            
            for book_idx in rated_books:
                book = available_books.iloc[book_idx]
                
                if book['genre'] in preferred_genres:
                    rating = np.random.choice([3, 4, 5], p=[0.2, 0.4, 0.4])
                else:
                    rating = np.random.choice([1, 2, 3, 4, 5], p=[0.1, 0.2, 0.4, 0.2, 0.1])
                
                rating = rating + np.random.normal(0, 0.3)
                rating = max(1.0, min(5.0, rating))
                
                ratings_data.append({
                    'user_id': user_id,
                    'book_id': book['book_id'],
                    'rating': round(rating, 1)
                })
    
    ratings_df = pd.DataFrame(ratings_data)
    
    if len(ratings_df) > target_ratings:
        ratings_df = ratings_df.sample(n=target_ratings, random_state=42).reset_index(drop=True)
    
    actual_sparsity = (1 - len(ratings_df) / (len(users_df) * len(books_df))) * 100
    print(f"Generated dataset with {actual_sparsity:.1f}% sparsity")
    print(f"Books: {len(books_df)}, Users: {len(users_df)}, Ratings: {len(ratings_df)}")
    
    return books_df, users_df, ratings_df

def generate_evaluation_data():
    """Generate additional data for system evaluation"""
    return generate_book_data()

if __name__ == "__main__":
    books, users, ratings = generate_book_data()
    print("Data generation completed successfully!")
    print(f"Generated {len(books)} books, {len(users)} users, and {len(ratings)} ratings")
