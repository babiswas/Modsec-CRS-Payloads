curl -X POST http://hello.app:4080 "Host: localhost" -H "User-Agent: ModSecurity CRS 3 Tests" -d "| echo '<?php include($_GET['page'])| ?>' > rf
i.php"