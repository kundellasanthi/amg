html>
    <head>
        <title>static variable</title>
</head>
<body>
    <?php
    function mytest()
    {
        static $num=0;
        echo "$num";
        $num++;
    }
    mytest();
    echo "$num";
    mytest();
    echo "$num";
    mytest();
    echo "$num";
    ?>
</body>
    </html>