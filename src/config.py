"""
Configuration Management for Flask Application
Loads environment variables and provides configuration classes for different environments.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration class with common settings."""
    
    # Application Settings
    APP_NAME = os.getenv('APP_NAME', 'DevOps Demo App')
    APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Server Settings
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5000))
    DEBUG = False
    
    # Environment
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')


class DevelopmentConfig(Config):
    """Development environment configuration."""
    
    DEBUG = True
    ENVIRONMENT = 'development'


class ProductionConfig(Config):
    """Production environment configuration."""
    
    DEBUG = False
    ENVIRONMENT = 'production'


class TestingConfig(Config):
    """Testing environment configuration."""
    
    TESTING = True
    DEBUG = True
    ENVIRONMENT = 'testing'


# Configuration mapping
config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config():
    """Get configuration based on environment variable."""
    env = os.getenv('ENVIRONMENT', 'development')
    return config_map.get(env, config_map['default'])
