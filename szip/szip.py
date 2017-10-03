from zipfile import *
import sys
import os
 
import click
 
 
def zipdir(adir, ziph):
	# ziph is zipfile handle
	for root, dirs, files in os.walk(adir):
		for file in files:
			apath = os.path.join(root, file)
			rpath = os.path.relpath(apath, adir)
			ziph.write(apath, rpath)
 
 
def compress_dir(src, dest):
	zipf = ZipFile(dest, 'w', ZIP_DEFLATED)
	zipdir(src, zipf)
	zipf.close()
 
 
def compress_file(src, dest):
	with ZipFile(dest, 'w', ZIP_DEFLATED) as myzip:
		rpath = os.path.basename(src)
		myzip.write(src, rpath)
 
 
@click.command()
@click.argument('source')
@click.option('--dest', default='new.zip', help="The name of the zipfile.")
def szip(source, dest):
	if os.path.isdir(source):
		compress_dir(source, dest)
	else:
		compress_file(source, dest)
 
 
if __name__ == '__main__':
	szip()