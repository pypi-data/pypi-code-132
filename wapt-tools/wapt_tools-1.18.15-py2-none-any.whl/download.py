import glob
import logging
import os
import requests
import shutil
import sys
from .hash import sha256sum

log = logging.getLogger(__name__)


def copy_tree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copy_tree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)


def save_url_to_file(url, pathname):
    if url.startswith('http'):
        try:
            r = requests.get(url, stream=True)
            if not r.ok:
                log.critical('failed to download {} from {}, 404 not found'.format(os.path.basename(pathname), url))
                sys.exit(1)

            with open(pathname, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            del r
        except Exception as e:
            log.critical('failed to download {} from {}, {}'.format(os.path.basename(pathname), url, e))
            sys.exit(1)
    elif url.startswith('file'):
        from_path = url[7:]
        if os.path.isdir(from_path):
            copy_tree(from_path, pathname)
        else:
            shutil.copy2(from_path, pathname)
    else:
        log.critical('failed to download {} from {}, invalid url'.format(os.path.basename(pathname), url))
        sys.exit(1)


def download(url, pathname, clean=True, checksum=None):
    """ Download the file at a given url and save it to pathname.

    The files existing in the same folder and with the same extension are removed if clean=True.

    Parameters
    ----------
    url: string
        url of the file to be dowloaded
    pathname: string
        pathname of the file to be saved
    clean: boolean
        cleanup needed
    checksum: string|None
        use checksum to validate download if not None
    """
    log.info('downloading {} from {}'.format(os.path.basename(pathname), url))

    extension = os.path.splitext(pathname)[1]
    dirname = os.path.dirname(pathname)

    if clean and extension != '':
        pattern = os.path.join(dirname, '*{}'.format(extension))
        log.debug('cleaning files {} except {}'.format(pattern, pathname))
        for file in glob.glob(pattern):
            if file != pathname:
                log.debug('removing {}'.format(file))
                os.remove(file)

    if not os.path.exists(pathname):
        save_url_to_file(url, pathname)
    else:
        if checksum:
            computed = sha256sum(pathname)
            if computed != checksum:
                log.info('{file} checksum mismatch, downloading'.format(file=pathname))
                os.remove(pathname)
                save_url_to_file(url, pathname)
        else:
            log.debug('{} already exists'.format(pathname))

    if checksum:
        computed = sha256sum(pathname)
        if computed != checksum:
            os.remove(pathname)
            log.critical('{file} checksum mismatch, downloaded file deleted'.format(file=pathname))
            sys.exit(1)


def download_all(files, folder, version=None, clean=True, use_checksum=True):
    """ Download all files described in files.

    The files existing in the same folder and with the same extension are removed if clean=True.

    Parameters
    ----------
    files: list
        files part of version-check.json
    folder: string
        folder to save downloaded files to
    vars: dict
        optional dict of key/value substitutions (e.g.: 'version': 1.2.3 => {version} => 1.2.3)
    clean: boolean
        cleanup needed
    use_checksum: boolean
        use checksum to validate download or not
    """
    if clean:
        log.debug('cleaning folder {}'.format(folder))
        for file in glob.glob(os.path.join(folder, '*')):
            log.debug('removing {}'.format(file))
            os.remove(file)

    for file in files:
        url = file['url_download_file']
        if sys.platform.startswith('linux'):
            url = url.replace('//fs-apps/', '/mnt/filesvr/')

        output = os.path.join(folder, file['output_file'])

        if version:
            url = url.replace('{version}', version)
            output = output.replace('{version}', version)

            version_no_dot = version.replace('.', '')
            url = url.replace('{version_no_dot}', version_no_dot)
            output = output.replace('{version_no_dot}', version_no_dot)

            v = version.split('.')
            version_2digits = v[0] + '.' + v[1]
            url = url.replace('{version_2digits}', version_2digits)
            output = output.replace('{version_no_dot}', version_2digits)

        log.debug('download {} from {}'.format(output, url))
        download(url, output, clean=False, checksum=file['checksum'] if use_checksum else None)
