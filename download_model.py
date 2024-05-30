from modelscope import snapshot_download

model_downloaded_path = snapshot_download(
    model_id="pzc163/chatTTS",
    cache_dir="ChatTTS/model" # 本地保存目录，默认为 ~/.cache/modelscope/hub
)

print("模型已保存：",model_downloaded_path)