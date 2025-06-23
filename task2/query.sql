## SQL Queries

### 1. Top 5 Brands by Receipts Scanned for the Most Recent Month

```sql
SELECT 
    b.brand_name,
    COUNT(DISTINCT r.receipt_id) AS receipt_count
FROM fact_receipt r
JOIN fact_receipt_item ri ON r.receipt_id = ri.receipt_id
JOIN dim_brand b ON ri.barcode = b.barcode
WHERE DATE_TRUNC('month', r.purchase_date) = DATE_TRUNC('month', CURRENT_DATE)
GROUP BY b.brand_name
ORDER BY receipt_count DESC
LIMIT 5;
```

### 2. Top 5 Brands by Receipts Scanned for the Previous Month

```sql
SELECT 
    b.brand_name,
    COUNT(DISTINCT r.receipt_id) AS receipt_count
FROM fact_receipt r
JOIN fact_receipt_item ri ON r.receipt_id = ri.receipt_id
JOIN dim_brand b ON ri.barcode = b.barcode
WHERE DATE_TRUNC('month', r.purchase_date) = DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
GROUP BY b.brand_name
ORDER BY receipt_count DESC
LIMIT 5;
```

### 3. Average Spend Comparison Between Accepted and Rejected Receipt Status

```sql
SELECT 
    receipt_status,
    AVG(total_spent) AS avg_spend
FROM fact_receipt
WHERE receipt_status IN ('Accepted', 'Rejected')
GROUP BY receipt_status;
```

### 4. Total Items Purchased for Accepted vs Rejected Receipt Status

```sql
SELECT 
    receipt_status,
    SUM(purchased_item_count) AS total_items
FROM fact_receipt
WHERE receipt_status IN ('Accepted', 'Rejected')
GROUP BY receipt_status;
```

---
