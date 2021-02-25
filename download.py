import argparse
from bing_image_downloader import downloader

parser = argparse.ArgumentParser(description='Download images from bing search.')
parser.add_argument('-q', required=True, action='store', type=str, help='The query to search.')
parser.add_argument('-limit', required=True, action='store', type=int, help='The limit of images to be downloaded.', default=10)

args = parser.parse_args()

downloader.download(args.q, limit=args.limit,  output_dir='dataset', adult_filter_off=True, force_replace=False)