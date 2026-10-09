import contextlib
import io
import runpy
import subprocess
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import build


class PublishTests(unittest.TestCase):
    def test_clean_working_tree_retries_push_without_new_commit(self):
        with patch.object(build.os.path, 'exists', return_value=False), \
                patch.object(build.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0)) as run:
            build.main()
        self.assertEqual([call.args[0] for call in run.call_args_list], [
            ['git', 'add', '.'], ['git', 'diff', '--cached', '--quiet'], ['git', 'push'],
        ])

    def test_staged_changes_are_committed_before_push(self):
        def result(command, **kwargs):
            return subprocess.CompletedProcess(command, 1 if command[1] == 'diff' else 0)

        with patch.object(build.os.path, 'exists', return_value=False), \
                patch.object(build.subprocess, 'run', side_effect=result) as run:
            build.main()
        commands = [call.args[0] for call in run.call_args_list]
        self.assertEqual(commands[2][:3], ['git', 'commit', '-m'])
        self.assertEqual(commands[3], ['git', 'push'])

    def test_cli_returns_git_push_failure_exit_code(self):
        def result(command, **kwargs):
            if command == ['git', 'push']:
                self.assertTrue(kwargs['check'])
                raise subprocess.CalledProcessError(1, command)
            return subprocess.CompletedProcess(command, 0)

        output = io.StringIO()
        with patch.object(build.os.path, 'exists', return_value=False), \
                patch.object(build.subprocess, 'run', side_effect=result), \
                contextlib.redirect_stderr(output), self.assertRaises(SystemExit) as error:
            runpy.run_path(str(Path(build.__file__)), run_name='__main__')
        self.assertEqual(error.exception.code, 1)
        self.assertIn('Publish failed: git push', output.getvalue())


if __name__ == '__main__':
    unittest.main()
