# AWS kintone Backup
To store all kintone record and form configurations to Amazon S3.

# Prepare
Configure dev.yml or prd.yml

|Key|Contents|
|---|---|
|KINTONE_DOMAIN|Your domain name of kintone|
|KINTONE_API_KEY|API key for target appllication|
|KINTONE_APP|kintone APP ID|
|S3_BUCKET|Bucket name of target Amazon S3|
|S3_OBJECT_PREFIX|Target object prefix name (after prefix, date characters will be attached)|

# Deploy

```sh
$ sls deploy [--stage prd/dev]
```
(Default stage is "dev")

