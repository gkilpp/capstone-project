SELECT
  date,
  fullVisitorId,
  visitId,
  visitNumber,
  channelGrouping,
  device.deviceCategory AS device,
  geoNetwork.country AS country,
  totals.visits,
  totals.pageviews,
  totals.transactions,
  totals.totalTransactionRevenue / 1000000 AS revenue
FROM `bigquery-public-data.google_analytics_sample.ga_sessions_*`