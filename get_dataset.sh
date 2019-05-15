
# original dataset is from https://captain-whu.github.io/DOAI2019/dataset.html
# processed by NTU DLCV spring 2019 TAs 

wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1KaHsgVEB4Yjp-86ZpOo15U5BuQvfPXDq' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1KaHsgVEB4Yjp-86ZpOo15U5BuQvfPXDq" -O dataset.zip && rm -rf /tmp/cookies.txt

# wget https://github.com/5loaves-2fish-12basckets/downloadable/releases/download/dset.dota.v1/dataset.zip
unzip dataset.zip
rm dataset.zip

