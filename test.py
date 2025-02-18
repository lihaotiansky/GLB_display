from urllib.parse import quote

# 原始模型 URL
model_url = "http://data.3d.vommatec.com/VOMMA_Lab/yud.glb?Expires=1737889132&OSSAccessKeyId=TMP.3Kfib8Dufo2BAR6V9a1UdvFGNZAmq7jKjvzGcTofJJKV667V6vVtqP4GGxz7ZvgTeNCNnmcFbLyoAvgsZffu7GptpKSBJi&Signature=bok7Gq2Gif%2F7wPFyjTgHwgfLlOo%3D";   
# 对 URL 进行编码
encoded_model_url = quote(model_url, safe='')

# 生成查看器 URL
viewer_url = f"http://3d.vommatec.com/?model={encoded_model_url}"

# 打印查看器 URL
print("Viewer URL:", viewer_url)