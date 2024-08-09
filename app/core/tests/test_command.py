from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.await_db.Command.check')
class CommandTest(SimpleTestCase):

    def test_check_db_status(self, patched_check):
        patched_check.return_value = True

        call_command('await_db')

        patched_check.assert_called_once_with(databases=['default'])

    def test_check_db_failure_attempt_count(self, patched_check):
        patched_check.side_effect = OperationalError()
        MAX_RETRIES: int = 5

        call_command('await_db')

        self.assertEqual(patched_check.call_count, MAX_RETRIES)