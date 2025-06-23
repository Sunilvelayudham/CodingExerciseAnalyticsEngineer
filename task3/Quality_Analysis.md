1. Missing Values

- Receipts Table
    bonusPointsEarned, bonusPointsEarnedReason, pointsEarned, pointsAwardedDate: High missing counts (≥500 records). These may be optional fields, but missing them reduces analytical depth.
    purchaseDate: Missing in 448 records – critical for time-based reporting (e.g., monthly spend, trends).
    rewardsReceiptItemList: Missing in 440 receipts – may indicate incomplete receipt captures.
    totalSpent, purchasedItemCount: Over 400 missing – impacts spend and item analysis.
    A - Action: Determine if these fields are optional or due to ingestion issues. Consider excluding or imputing during aggregation.

- Users Table
    lastLogin, signUpSource, and state have missing values:
    lastLogin: 62 missing – could indicate dormant accounts.
    signUpSource: 48 missing – affects attribution analytics.
    state: 56 missing – impacts geo-level reporting.
    A - Action: Set default categories like "Unknown" or "Inactive", especially for role-based and geo-segmented analytics.

- Brands Table
    category, categoryCode, brandCode, and topBrand have missing values:
    categoryCode: 650 missing – problematic for category-based rollups.
    topBrand: 612 missing – reduces ability to analyze brand positioning.
    A - Action: Clean and backfill if possible. If not, exclude from category-based aggregations or apply null-safe handling.


2. Invalid Price Check
    4 receipt items have negative or zero prices.
    Action: Flag for cleanup or manual validation; such entries distort financial metrics.

3. Missing Barcode or Description
    4,291 items are missing barcode – cannot be linked to brands, reducing join completeness.
    173 descriptions are “ITEM NOT FOUND” – may be unrecognized SKUs.
    Action: Consider a fallback mapping or manual review pipeline.
        Tag “ITEM NOT FOUND” as unclassified items for exclusion or special reporting.

4. Duplicate Records
    283 duplicate users (_id field).
    Action: Review if duplicate _ids are truly identical or shadow copies. De-duplicate based on unique constraints (email, sign-up date, etc.).


5. Orphan Barcodes
    7,381 items have barcodes not found in brands – indicates a weak relationship between receipt items and brand catalog.
    Action: Suggest batch enrichment or reconciliation.
        Build a process to capture new/unmapped barcodes into a staging layer for review.

6. Logical Consistency
    No receipts where pointsEarned < bonusPointsEarned – good sign; business rules are respected here.