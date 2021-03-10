==========
2-BM tools
==========


`2bm tools <https://github.com/xray-imaging/2bm-tools>`_ is a collection of Python script avaialble for user operation.

Usage
-----

Install from `Anaconda <https://www.anaconda.com/distribution/>`_ python3.x, then install 2bm tools::

    $ git clone https://github.com/xray-imaging/2bm-tools.git
    $ cd 2bm-tools


at 2-BM can then run any of the 2bm tools with::

    [user2bmb@arcturus]$ bash
    [user2bmb@arcturus]$ cd /local/user2bmb/conda/2bm-tools/

then select one of the tool, for example to log the 2-BM furnace temperature::

    [user2bmb@arcturus]$ python log_temp.py

    2021-03-10 15:22:25,652 - Temperature: 24.0000 Â°C;  /local/data/2021-03/Testing/test_151.h5
    2021-03-10 15:22:30,657 - Temperature: 24.0000 Â°C;  /local/data/2021-03/Testing/test_151.h5
    2021-03-10 15:22:35,663 - Temperature: 24.0000 Â°C;  /local/data/2021-03/Testing/test_151.h5
    2021-03-10 15:22:38,867 - interrupted!
    2021-03-10 15:22:38,867 - Log information saved at: /home/beams/USER2BMB/logs/temperature_2021-03-10_15:22:25.log
