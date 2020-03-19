package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class CoverageLongsTest {
    long[] hashes;
    int count=3;
    double ratio=3.14;

    @Before
    public void setUp() throws Exception {
        hashes=new long[]{40,36,34};

    }

    @After
    public void tearDown() throws Exception {
        hashes=null;
        assertNull(hashes);
    }
    @Test
    public void getHashes() {//測試CoverageLongs的getHashes 比對參數陣列與回傳陣列內容是否相同

        CoverageLongs coverageLongs=new CoverageLongs(hashes,count,ratio);
        assertArrayEquals(hashes,coverageLongs.getHashes());

    }

    @Test
    public void getRatio() {//測試參數ratio與回傳ratio是否同一數字

        CoverageLongs coverageLongs=new CoverageLongs(hashes,count,ratio);
        assertEquals(ratio,coverageLongs.getRatio(),0.00001);
    }

    @Test
    public void getHashLength() {//只取陣列中第一個元素的前四個位元 測試10001 AND 000001111 結果為1
        long[] hashes=new long[]{17,36,34};

        CoverageLongs coverageLongs=new CoverageLongs(hashes,count,ratio);
        assertEquals(1,coverageLongs.getHashLength());
    }
    @Test
    public void getHashLength_sizeZero() {//當hashes鎮列為0個元素 回傳為0
        long[] hashes=new long[]{};
        int count=0;
        CoverageLongs coverageLongs=new CoverageLongs(hashes,count,ratio);
        assertEquals(0,coverageLongs.getHashLength());
    }
//    @Test
//    public void testToString() {
//        long[] hashes=new long[]{17,36,34};
//        int count=3;
//        double ratio=3.14;
//        CoverageLongs coverageLongs=new CoverageLongs(hashes,count,ratio);
//        assertEquals("Coverage [hashes=" + coverageLongs.getHashes().toString() + ", ratio=" + ratio + "]",coverageLongs.toString());
//
//    }

    @Test
    public void getCount() {//測試hash的元素共有幾個 我以3個為例子

        CoverageLongs coverageLongs=new CoverageLongs(hashes,count,ratio);
        assertEquals(3,coverageLongs.getCount());
    }


}