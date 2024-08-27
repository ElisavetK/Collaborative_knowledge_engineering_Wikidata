# Collaborative_knowledge_engineering_Wikidata
This repository includes scripts and data used to analyse Wikidata discussions for my paper "An analysis of discussions in collaborative knowledge engineering through the lens of Wikidata" (https://www.sciencedirect.com/science/article/pii/S1570826823000288).

## File description
Here is the description of the files.

**download_Wikidata_dumps**: This is a script to download Wikidata xml dumps from https://dumps.wikimedia.org/wikidatawiki/ .

**crawl_for_Project_chat.py**: This is a script to crawl the Wikidata interface and extract the included discussions.

**process_Wikidata_dumps.py**: This is a script to process the xml files and extract pages for item and property talk pages.

**data**: This folder includes the sample of discussions used for the thematic analysis.

**text_statistics.py**: This notebook processes the talk pages to separate threads and posts, and to count the words.

**statistical_tests.py**: This script includes statistical tests for the thematic analysis results.
