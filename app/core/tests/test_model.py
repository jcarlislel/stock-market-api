"""
Tests for models
"""
from django.test import TestCase
from core.models import UserManager
from django.contrib.auth import get_user_model

import logging

logging.basicConfig(level=logging.DEBUG)

class ModelTests(TestCase):

    def test_create_user_successful(self):
        """
        Test to create standard user
        """

        email: str = 'sample@example.com'
        password: str = 'password1234'

        user = get_user_model().objects.create_user(
            email,
            password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        """
        Test to check if email created will be normalized
        """

        manager: UserManager = get_user_model().objects

        list_of_emails = [
            ['sample@EXAMPLE.com', 'sample@example.com'],
            ['Testsample@Example.com', 'Testsample@example.com']
        ]
        password: str = 'password1234'

        for current_email, expected_email in list_of_emails:
            user = manager.create_user(
                current_email,
                password,                
            )

            self.assertEqual(user.email, expected_email)

    def test_if_email_exists(self):
        """
        Test to check if email field exists
        """

        null_email = None
        empty_email = ""
        password: str = 'password1234'

        manager: UserManager = get_user_model().objects

        # Check if email is NoneType
        with self.assertRaises(ValueError):
            manager.create_user(
                null_email,
                password,
            )
        # Check if email is provided but empty
        with self.assertRaises(ValueError):
            manager.create_user(
                empty_email,
                password,
            )            

    def test_create_super_user_successful(self):
        """
        Test to create standard user
        """

        email: str = 'sample_super_user@example.com'
        password: str = 'password1234'

        user = get_user_model().objects.create_superuser(
            email,
            password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.check_password(password))