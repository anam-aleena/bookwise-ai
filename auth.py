import streamlit as st
import pandas as pd
import hashlib
import os
from datetime import datetime

class AuthSystem:
    def __init__(self, users_file='users_credentials.csv'):
        self.users_file = users_file
        self._init_users_file()
    
    def _init_users_file(self):
        if not os.path.exists(self.users_file):
            df = pd.DataFrame({'username': [], 'password_hash': [], 'email': [], 'created_at': []})
            df.to_csv(self.users_file, index=False)
    
    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def signup(self, username, password, email):
        df = pd.read_csv(self.users_file)
        
        if username in df['username'].values:
            return False, "Username already exists"
        
        if email in df['email'].values:
            return False, "Email already registered"
        
        if len(username) < 3:
            return False, "Username must be at least 3 characters"
        
        if len(password) < 6:
            return False, "Password must be at least 6 characters"
        
        new_user = pd.DataFrame([{
            'username': username,
            'password_hash': self._hash_password(password),
            'email': email,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }])
        
        df = pd.concat([df, new_user], ignore_index=True)
        df.to_csv(self.users_file, index=False)
        
        return True, "Account created successfully!"
    
    def login(self, username, password):
        df = pd.read_csv(self.users_file)
        
        user = df[df['username'] == username]
        
        if user.empty:
            return False, "Username not found"
        
        if user.iloc[0]['password_hash'] != self._hash_password(password):
            return False, "Incorrect password"
        
        return True, "Login successful!"
    
    def get_user_info(self, username):
        df = pd.read_csv(self.users_file)
        user = df[df['username'] == username]
        
        if not user.empty:
            return user.iloc[0].to_dict()
        return None

def render_auth_page():
    st.markdown("""
    <style>
        .auth-container {
            max-width: 500px;
            margin: 0 auto;
            padding: 3rem 2rem;
        }
        .auth-header {
            text-align: center;
            color: #1f77b4;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        .auth-subheader {
            text-align: center;
            color: #666;
            font-size: 1rem;
            margin-bottom: 2rem;
        }
        .welcome-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            text-align: center;
        }
        .feature-list {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            margin-top: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    
    st.markdown('<h1 class="auth-header">📚 BookWise</h1>', unsafe_allow_html=True)
    st.markdown('<p class="auth-subheader">AI-Powered Book Recommendation System</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="welcome-box">
        <h2>Welcome to BookWise!</h2>
        <p>Discover your next favorite book with our intelligent recommendation system powered by advanced machine learning algorithms.</p>
    </div>
    """, unsafe_allow_html=True)
    
    auth = AuthSystem()
    
    tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign Up"])
    
    with tab1:
        st.subheader("Login to Your Account")
        
        login_username = st.text_input("Username", key="login_username", placeholder="Enter your username")
        login_password = st.text_input("Password", type="password", key="login_password", placeholder="Enter your password")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Login", use_container_width=True, type="primary"):
                if login_username and login_password:
                    success, message = auth.login(login_username, login_password)
                    if success:
                        st.session_state.authenticated = True
                        st.session_state.username = login_username
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.warning("Please enter both username and password")
    
    with tab2:
        st.subheader("Create a New Account")
        
        signup_username = st.text_input("Username", key="signup_username", placeholder="Choose a username (min 3 characters)")
        signup_email = st.text_input("Email", key="signup_email", placeholder="Enter your email address")
        signup_password = st.text_input("Password", type="password", key="signup_password", placeholder="Choose a password (min 6 characters)")
        signup_password_confirm = st.text_input("Confirm Password", type="password", key="signup_password_confirm", placeholder="Confirm your password")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("✨ Create Account", use_container_width=True, type="primary"):
                if signup_username and signup_email and signup_password and signup_password_confirm:
                    if signup_password != signup_password_confirm:
                        st.error("Passwords do not match!")
                    else:
                        success, message = auth.signup(signup_username, signup_password, signup_email)
                        if success:
                            st.success(message)
                            st.info("You can now login with your credentials!")
                        else:
                            st.error(message)
                else:
                    st.warning("Please fill in all fields")
    
    st.markdown("""
    <div class="feature-list">
        <h3>🎯 What You'll Get:</h3>
        <ul>
            <li>🤖 <b>6 Advanced ML Algorithms</b> - Hybrid ensemble, collaborative filtering, content-based & more</li>
            <li>📊 <b>Personalized Recommendations</b> - Tailored to your unique reading preferences</li>
            <li>📈 <b>Analytics Dashboard</b> - Track your reading patterns and discover insights</li>
            <li>🎨 <b>Beautiful Interface</b> - Modern, intuitive design for the best experience</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def check_authentication():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if 'username' not in st.session_state:
        st.session_state.username = None
    
    if not st.session_state.authenticated:
        render_auth_page()
        st.stop()

def logout():
    st.session_state.authenticated = False
    if 'username' in st.session_state:
        del st.session_state.username
    st.rerun()
