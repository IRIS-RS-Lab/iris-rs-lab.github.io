import datetime
import os
import subprocess
import sys


def main():
    date = datetime.date.today().strftime('%Y%m%d')

    # 自动修复缺失的栅格图
    if os.path.exists('scripts/fix_images.py'):
        subprocess.run([sys.executable, 'scripts/fix_images.py'], check=True)

    subprocess.run(['git', 'add', '.'], check=True)
    changes = subprocess.run(['git', 'diff', '--cached', '--quiet'])
    if changes.returncode == 1:
        subprocess.run(['git', 'commit', '-m', 'updated site %s' % date], check=True)
    elif changes.returncode != 0:
        raise subprocess.CalledProcessError(changes.returncode, changes.args)
    subprocess.run(['git', 'push'], check=True)


if __name__ == '__main__':
    try:
        main()
    except subprocess.CalledProcessError as error:
        print('Publish failed: %s (exit code %s).' % (' '.join(error.cmd), error.returncode), file=sys.stderr)
        sys.exit(error.returncode)
