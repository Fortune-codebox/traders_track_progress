"""
Test custom Django management commands
"""
from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import DatabaseError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandsTest(SimpleTestCase):
    """Test Commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test Waiting for database if db ready."""

        patched_check.return_value = True

        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for db when gettin OperationalError."""
        patched_check.side_effect = [DatabaseError] * 5 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
