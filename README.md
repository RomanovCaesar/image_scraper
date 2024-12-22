# image_scraper

---

# 基于Scrapy框架的图片爬取项目

该项目是一个基于Scrapy框架的网络爬虫，旨在从指定网页下载所有图片并将其保存到本地目录中。目标网页为：
`https://caesaugu.com/hosthatch%e7%91%9e%e5%a3%ab%e8%8b%8f%e9%bb%8e%e4%b8%96vps%e6%b5%8b%e8%af%84/`

## 功能特点

- 自动提取指定网页中的所有图片链接。
- 下载图片并保存到本地目录。
- 使用 Scrapy 内置的 `ImagesPipeline` 处理图片下载。

## 环境要求

- Python 3.6 或更高版本
- Scrapy 2.x 或更高版本
- Pillow 库（用于处理图片）

## 安装步骤

1. 克隆此仓库：

   ```bash
   git clone https://github.com/your-repository/image_scraper.git
   cd image_scraper
   ```

2. 安装依赖项：

   ```bash
   pip install scrapy pillow
   ```

## 使用方法

1. 创建 Scrapy 项目（如果尚未创建）：

   ```bash
   scrapy startproject image_scraper
   ```

2. 在 `items.py` 文件中定义一个用于保存图片 URL 的 Item 类：

   ```python
   class ImageScraperItem(scrapy.Item):
       image_urls = scrapy.Field()
   ```

3. 将爬虫脚本（`imagespider.py`）添加到 `image_scraper\spiders` 目录中。

4. 在 `settings.py` 文件中配置图片管道：

   ```python
   ITEM_PIPELINES = {
       'scrapy.pipelines.images.ImagesPipeline': 1,
   }
   IMAGES_STORE = 'images'
   ```

5. 运行爬虫：

   ```bash
   scrapy crawl imagespider
   ```

6. 下载的图片将保存在 `images` 文件夹中。

## 爬虫详细信息

- **爬虫名称**: `imagespider`
- **目标网址**: `https://caesaugu.com/hosthatch%e7%91%9e%e5%a3%ab%e8%8b%8f%e9%bb%8e%e4%b8%96vps%e6%b5%8b%e8%af%84/`
- **提取方法**: 使用 CSS 选择器提取图片 URL： 
```python
response.css('img::attr(src)').getall()
````

## 注意事项

- 爬取他人网站时，请遵守目标网站的服务条款和 robots.txt 文件规定。
- 禁止将此爬虫用于未经授权的数据抓取或非法用途。

## 许可证

该项目使用 MIT 许可证。详情请参见 [LICENSE](LICENSE) 文件。

---

### 备注：
- 您可以根据需要，修改该爬虫爬取图片的目标网址为您需要的网址。
