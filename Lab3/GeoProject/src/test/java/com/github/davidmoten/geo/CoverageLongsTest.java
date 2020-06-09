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

//------------------------------------------------------------------------------------------------------

    @Test
    public void getRatio_T1() {//測試參數ratio與回傳ratio是否同一數字

        CoverageLongs coverageLongs=new CoverageLongs(hashes,count,-3.14);
        assertEquals(-3.14,coverageLongs.getRatio(),0.00001);
    }
    @Test
    public void getRatio_T2() {//測試參數ratio與回傳ratio是否同一數字

        CoverageLongs coverageLongs=new CoverageLongs(hashes,count,0);
        assertEquals(0,coverageLongs.getRatio(),0.00001);
    }
    @Test
    public void getRatio_T3() {//測試參數ratio與回傳ratio是否同一數字

        CoverageLongs coverageLongs=new CoverageLongs(hashes,count,3.14);
        assertEquals(3.14,coverageLongs.getRatio(),0.00001);
    }
//------------------------------------------------------------------------------------------------------

    @Test
    public void getCount_T1() {//測試hash的元素共有幾個 我以3個為例子

        CoverageLongs coverageLongs=new CoverageLongs(hashes,-3,ratio);
        assertEquals(-3,coverageLongs.getCount());
    }
    @Test
    public void getCount_T2() {//測試hash的元素共有幾個 我以3個為例子

        CoverageLongs coverageLongs=new CoverageLongs(hashes,0,ratio);
        assertEquals(0,coverageLongs.getCount());
    }
    @Test
    public void getCount_T3() {//測試hash的元素共有幾個 我以3個為例子

        CoverageLongs coverageLongs=new CoverageLongs(hashes,3,ratio);
        assertEquals(3,coverageLongs.getCount());
    }
//------------------------------------------------------------------------------------------------------

    @Test
    public void getHashLength_T1() {
        long[] arr=new long[]{-10,38,23};

        CoverageLongs cls=new CoverageLongs(arr,count,ratio);
        assertEquals(6,cls.getHashLength());
    }
    @Test
    public void getHashLength_T2() {
        long[] arr=new long[]{0,38,23};

        CoverageLongs cls=new CoverageLongs(arr,count,ratio);
        assertEquals(0,cls.getHashLength());
    }
    @Test
    public void getHashLength_T3() {
        long[] arr=new long[]{10,38,23};

        CoverageLongs cls=new CoverageLongs(arr,count,ratio);
        assertEquals(10,cls.getHashLength());
    }
//------------------------------------------------------------------------------------------------------
    @Test
    public void toStringTest() {
        long[] arr=new long[]{10,38,23};

        CoverageLongs cls=new CoverageLongs(arr,count,ratio);
        cls.toString();
    }
}