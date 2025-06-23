# Data Quality Check for Receipt Data Warehouse

This repository contains a Python script to identify data quality issues in sample receipt, user, and brand datasets.

## 📁 Folder Structure

├── data/
│ ├── receipts.json
│ ├── users.json
│ └── brands.json
├── data_quality_check.py
└── README.md



## 🧪 What It Checks

- Missing or null values
- Negative or zero prices in receipt items
- Missing barcodes and suspicious descriptions ("ITEM NOT FOUND")
- Duplicate records in users and receipts
- Invalid joins (receipt items with barcodes not in brand data)
- Logical inconsistencies (e.g., `pointsEarned` < `bonusPointsEarned`)

## 🚀 How to Run

Ensure you have Python and pandas installed:

```bash
pip install pandas
python data_quality_check.py

Output
The script prints summary statistics and counts of detected data quality issues to the terminal.

=== Missing Values Check ===
Receipts:
 _id                          0
bonusPointsEarned          575
bonusPointsEarnedReason    575
createDate                   0
dateScanned                  0
finishedDate               551
modifyDate                   0
pointsAwardedDate          582
pointsEarned               510
purchaseDate               448
purchasedItemCount         484
rewardsReceiptItemList     440
rewardsReceiptStatus         0
totalSpent                 435
userId                       0
dtype: int64

Users:
 _id              0
active           0
createdDate      0
lastLogin       62
role             0
signUpSource    48
state           56
dtype: int64

Brands:
 _id               0
barcode           0
category        155
categoryCode    650
cpg               0
name              0
topBrand        612
brandCode       234
dtype: int64

=== Invalid Price Check ===
Items with invalid prices: 4

=== Missing Barcode or Description ===
Items missing barcode: 4291
Items with 'ITEM NOT FOUND' description: 173

=== Duplicate Checks ===
Duplicate users: 283
Duplicate receipts: 0

=== Orphan Barcode Check ===
Items with barcodes not in brand list: 7381

=== Logical Consistency Check ===
Receipts where pointsEarned < bonusPointsEarned: 0

=== Done ===
