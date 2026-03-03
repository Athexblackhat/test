<?php
// ULTRA SIMPLE IP LOGGER - GUARANTEED TO WORK
// No fancy features, just pure functionality

// Turn off all errors completely
error_reporting(0);
ini_set('display_errors', 0);

// Start output buffering
ob_start();

// Create simple log directory
$logDir = 'shadow_logs';
if (!file_exists($logDir)) {
    mkdir($logDir, 0777, true);
}

// Get basic info
$ip = $_SERVER['REMOTE_ADDR'];
$userAgent = $_SERVER['HTTP_USER_AGENT'] ?? 'Unknown';
$timestamp = date('Y-m-d H:i:s');
$date = date('Y-m-d');

// Simple text log (NO CSV, NO JSON, just plain text)
$logFile = $logDir . '/visitors_' . $date . '.txt';
$logEntry = "[$timestamp] IP: $ip | UA: $userAgent" . PHP_EOL;
file_put_contents($logFile, $logEntry, FILE_APPEND);

// Clear output buffer
ob_clean();

// Check request type and respond appropriately
if (isset($_GET['debug'])) {
    // Show debug info
    header('Content-Type: text/html');
    echo "<!DOCTYPE html>";
    echo "<html><body style='background:#000;color:#0f0;font-family:monospace;padding:20px;'>";
    echo "<h1>✅ IP LOGGED SUCCESSFULLY</h1>";
    echo "<p><strong>Your IP:</strong> $ip</p>";
    echo "<p><strong>Time:</strong> $timestamp</p>";
    echo "<p><strong>Log file:</strong> $logFile</p>";
    echo "<p><a href='?image' style='color:#0f0;'>View tracking pixel</a></p>";
    echo "</body></html>";
    ob_end_flush();
    exit();
}

// Default: Return 1x1 transparent pixel (for tracking)
header('Content-Type: image/png');
echo base64_decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==');
ob_end_flush();
exit();
?>
