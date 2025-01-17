from pathlib import Path
import subprocess
import sys

def main():
    subprocess.run(['ffmpeg', '-i', filename, '-metadata', f'{key}={value}', '-codec', 'copy', output])

if __name__ == '__main__':
    sys.exit(main())
