import pandas as pd
import json

# Load data
receipts = pd.read_json('data/receipts.json', lines=True)
users = pd.read_json('data/users.json', lines=True)
brands = pd.read_json('data/brands.json', lines=True)

# Normalize nested receipt item list
receipt_items_raw = receipts[['rewardsReceiptItemList', '_id']].explode('rewardsReceiptItemList').reset_index(drop=True)
receipt_items = pd.json_normalize(receipt_items_raw['rewardsReceiptItemList'])
receipt_items['receipt_id'] = receipt_items_raw['_id']

print("\n=== Missing Values Check ===")
print("Receipts:\n", receipts.isnull().sum())
print("\nUsers:\n", users.isnull().sum())
print("\nBrands:\n", brands.isnull().sum())

print("\n=== Invalid Price Check ===")
invalid_prices = receipt_items[
    (receipt_items['finalPrice'].astype(float) <= 0) |
    (receipt_items['itemPrice'].astype(float) <= 0)
]
print(f"Items with invalid prices: {len(invalid_prices)}")

print("\n=== Missing Barcode or Description ===")
print(f"Items missing barcode: {receipt_items['barcode'].isnull().sum()}")
print(f"Items with 'ITEM NOT FOUND' description: {receipt_items['description'].str.upper().eq('ITEM NOT FOUND').sum()}")

print("\n=== Duplicate Checks ===")
print(f"Duplicate users: {users.duplicated('_id').sum()}")
print(f"Duplicate receipts: {receipts.duplicated('_id').sum()}")

print("\n=== Orphan Barcode Check ===")
invalid_barcodes = receipt_items[~receipt_items['barcode'].isin(brands['barcode'])]
print(f"Items with barcodes not in brand list: {len(invalid_barcodes)}")

print("\n=== Logical Consistency Check ===")
receipts['pointsEarned'] = receipts['pointsEarned'].astype(float)
receipts['bonusPointsEarned'] = receipts['bonusPointsEarned'].astype(float)
invalid_points = receipts[receipts['pointsEarned'] < receipts['bonusPointsEarned']]
print(f"Receipts where pointsEarned < bonusPointsEarned: {len(invalid_points)}")

print("\n=== Done ===")
