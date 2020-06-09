package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.HashSet;
import java.util.Set;

import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;

public class CoverageTest {
    Set<String> hashes;
    @Before
    public void setUp() throws Exception {
        hashes = new HashSet<String>();
    }

    @After
    public void tearDown() throws Exception {
        hashes=null;
        assertNull(hashes);
    }


    @Test
    public void Coverage() { //測試Coverage有參數的建構子 將CoverageLongs轉換為Coverage 並測試其中的getRatio()、getHashLength()
        long[] hashes=new long[]{101,100,1};
        int count=3;
        double ratio=3.14;
        CoverageLongs coverageLongs=new CoverageLongs(hashes,count,ratio);
        Coverage coverage=new Coverage(coverageLongs);
        assertEquals(3.14,coverage.getRatio(),0.00001);
        assertEquals(1,coverage.getHashLength());
    }

    @Test
    public void getHashes() {//測試參數陣列與回傳陣列是否為同一記憶體位置

        hashes.add("number1");
        hashes.add("number2");
        hashes.add("number3");
        hashes.add("number4");

        Coverage coverage=new Coverage(hashes,3.14);
        assertEquals(hashes,coverage.getHashes());
    }

    @Test
    public void getRatio() {//測試傳入參數與回傳參數是否為同一個數字
        Coverage coverage=new Coverage(hashes,3.14);
        assertEquals(3.14,coverage.getRatio(),0.00001);
    }

    @Test
    public void getHashLength() {//測試陣列第一個元素共有多少字元

        hashes.add("number1");
        hashes.add("number2");
        hashes.add("number3");
        hashes.add("number4");

        Coverage coverage=new Coverage(hashes,3.14);
        assertEquals(7,coverage.getHashLength());
    }
    @Test
    public void getHashLength_sizeZero() {//測試陣列沒有元素應回傳0字元


        Coverage coverage=new Coverage(hashes,3.14);
        assertEquals(0,coverage.getHashLength());
    }
    @Test
    public void testToString() {//測試Coverage轉字串訊息
        double ratio=3.14;
        Coverage coverage=new Coverage(hashes,ratio);
        assertEquals("Coverage [hashes=" + coverage.getHashes() + ", ratio=" + ratio + "]",coverage.toString());

    }


}