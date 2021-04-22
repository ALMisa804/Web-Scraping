{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "import requests\n",
    "import pymongo\n",
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars news\n",
    "\n",
    "url = 'https://mars.nasa.gov/news/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.visit(url)\n",
    "time.sleep(3)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "slides = soup.find_all('li', class_='slide')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"NASA's Ingenuity Mars Helicopter Logs Second Successful Flight\""
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "content_title = slides[0].find('div', class_ = 'content_title')\n",
    "news_title = content_title.text.strip()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The small rotorcraft’s horizons were expanded on its second flight.'"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "article_teaser_body = slides[0].find('div', class_ = 'article_teaser_body')\n",
    "news_p = article_teaser_body.text.strip()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "# JPL Mars space images\n",
    "\n",
    "jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'\n",
    "featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'\n",
    "browser.visit(featured_image_url)\n",
    "html = browser.html\n",
    "images_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.htmlhttps://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg\n"
     ]
    }
   ],
   "source": [
    "image_path = images_soup.find_all('img')[-1][\"src\"]\n",
    "featured_image_url = jpl_url + image_path\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                      0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers,\n",
       "   Mars - Earth Comparison             Mars            Earth\n",
       " 0               Diameter:         6,779 km        12,742 km\n",
       " 1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 2                  Moons:                2                1\n",
       " 3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 4         Length of Year:   687 Earth days      365.24 days\n",
       " 5            Temperature:     -87 to -5 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Mars facts\n",
    "\n",
    "facts_url = 'https://space-facts.com/mars/'\n",
    "tables = pd.read_html(facts_url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Description</th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Description                          Value\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_facts_df = tables[2]\n",
    "mars_facts_df.columns = [\"Description\", \"Value\"]\n",
    "mars_facts_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<table border=\"1\" class=\"dataframe\">\n",
      "  <thead>\n",
      "    <tr style=\"text-align: right;\">\n",
      "      <th></th>\n",
      "      <th>Description</th>\n",
      "      <th>Value</th>\n",
      "    </tr>\n",
      "  </thead>\n",
      "  <tbody>\n",
      "    <tr>\n",
      "      <th>0</th>\n",
      "      <td>Equatorial Diameter:</td>\n",
      "      <td>6,792 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>1</th>\n",
      "      <td>Polar Diameter:</td>\n",
      "      <td>6,752 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>2</th>\n",
      "      <td>Mass:</td>\n",
      "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>3</th>\n",
      "      <td>Moons:</td>\n",
      "      <td>2 (Phobos &amp; Deimos)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>4</th>\n",
      "      <td>Orbit Distance:</td>\n",
      "      <td>227,943,824 km (1.38 AU)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>5</th>\n",
      "      <td>Orbit Period:</td>\n",
      "      <td>687 days (1.9 years)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>6</th>\n",
      "      <td>Surface Temperature:</td>\n",
      "      <td>-87 to -5 °C</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>7</th>\n",
      "      <td>First Record:</td>\n",
      "      <td>2nd millennium BC</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>8</th>\n",
      "      <td>Recorded By:</td>\n",
      "      <td>Egyptian astronomers</td>\n",
      "    </tr>\n",
      "  </tbody>\n",
      "</table>\n"
     ]
    }
   ],
   "source": [
    "mars_html_table = mars_facts_df.to_html()\n",
    "mars_html_table.replace('\\n', '')\n",
    "print(mars_html_table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars hemispheres\n",
    "\n",
    "base_url = 'https://astrogeology.usgs.gov'\n",
    "url = base_url + '/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "items = soup.find_all('div', class_='item')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['Cerberus Hemisphere Enhanced',\n",
       " 'Schiaparelli Hemisphere Enhanced',\n",
       " 'Syrtis Major Hemisphere Enhanced',\n",
       " 'Valles Marineris Hemisphere Enhanced']"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "urls = []\n",
    "titles = []\n",
    "for item in items:\n",
    "    urls.append(base_url + item.find('a')['href'])\n",
    "    titles.append(item.find('h3').text.strip())\n",
    "print(urls)\n",
    "titles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "browser.visit(urls[0])\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "oneurl = base_url+soup.find('img',class_='wide-image')['src']\n",
    "oneurl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg',\n",
       " 'https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg',\n",
       " 'https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg',\n",
       " 'https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg']"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img_urls = []\n",
    "for oneurl in urls:\n",
    "    browser.visit(oneurl)\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    oneurl = base_url+soup.find('img',class_='wide-image')['src']\n",
    "    img_urls.append(oneurl)\n",
    "    \n",
    "img_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}]"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls = []\n",
    "\n",
    "for i in range(len(titles)):\n",
    "    hemisphere_image_urls.append({'title':titles[i],'img_url':img_urls[i]})\n",
    "\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cerberus Hemisphere Enhanced\n",
      "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg\n",
      "\n",
      "Schiaparelli Hemisphere Enhanced\n",
      "https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg\n",
      "\n",
      "Syrtis Major Hemisphere Enhanced\n",
      "https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg\n",
      "\n",
      "Valles Marineris Hemisphere Enhanced\n",
      "https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg\n",
      "\n"
     ]
    }
   ],
   "source": [
    "for i in range(len(hemisphere_image_urls)):\n",
    "    print(hemisphere_image_urls[i]['title'])\n",
    "    print(hemisphere_image_urls[i]['img_url'] + '\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
