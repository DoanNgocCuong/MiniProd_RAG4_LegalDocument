Từ file `app.py`, tôi thấy có một số định dạng JSON được sử dụng trong các API endpoint khác nhau:

1. **Endpoint `/crawl` (POST)**:
```json
{
    "url": "URL_trang_web",
    "company_name": "tên_công_ty",
    "max_links": 10  // không bắt buộc, mặc định là 10
}
```

2. **Endpoint `/save_db` (POST)**:
```json
{
    "company_name": "tên_collection"
}
```

3. **Endpoint `/change_collection` (POST)**:
```json
{
    "collection_name": "tên_collection"
}
```

4. **Endpoint `/send_message` (POST)**:
```json
{
    "question": "câu_hỏi_của_người_dùng"
}
```

Các Response JSON:

1. **Từ `/get_collections` (GET)**:
```json
{
    "collections": ["collection1", "collection2", "..."]
}
```

2. **Từ `/send_message`**:
```json
{
    "response": "câu_trả_lời",
    "links": ["link1", "link2", "..."]
}
```

3. **Từ `/crawl_status` (GET)**:
```json
{
    "status": "thông_tin_về_trạng_thái_crawl",
    // các thông tin khác về tiến trình crawl
}
```

4. **Từ `/health` (GET)**:
```json
{
    "status": "healthy"
}
```

File này đọc dữ liệu từ file JSON ở đường dẫn `data/raw/outputs.json` (cho việc lưu DB) và `data/raw/status.json` (cho việc theo dõi trạng thái crawl).
