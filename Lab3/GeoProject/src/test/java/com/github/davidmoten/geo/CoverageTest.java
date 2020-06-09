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


//------------------------------------------------------------------------------------------------------

    @Test
    public void getHashes_T1() {//測試參數陣列與回傳陣列是否為同一記憶體位置
        hashes = new HashSet<String>();

        Coverage coverage=new Coverage(hashes,3.14);
        assertEquals(0,coverage.getHashes().size());
    }

    @Test
    public void getHashes_T2() {//測試參數陣列與回傳陣列是否為同一記憶體位置

        hashes.add("number1");
        hashes.add("number2");
        hashes.add("number3");
        hashes.add("number4");

        Coverage coverage=new Coverage(hashes,3.14);
        assertEquals(4,coverage.getHashes().size());
    }


//------------------------------------------------------------------------------------------------------

    @Test
    public void getRatio_T1() {//測試傳入參數與回傳參數是否為同一個數字
        Coverage coverage=new Coverage(hashes,-3.14);
        assertEquals(-3.14,coverage.getRatio(),0.00001);
    }

    @Test
    public void getRatio_T2() {//測試傳入參數與回傳參數是否為同一個數字
        Coverage coverage=new Coverage(hashes,0);
        assertEquals(0,coverage.getRatio(),0.00001);
    }
    @Test
    public void getRatio_T3() {//測試傳入參數與回傳參數是否為同一個數字
        Coverage coverage=new Coverage(hashes,3.14);
        assertEquals(3.14,coverage.getRatio(),0.00001);
    }
//------------------------------------------------------------------------------------------------------
    @Test
    public void getHashLength_T1() {//測試陣列沒有元素應回傳0字元


        Coverage coverage=new Coverage(hashes,3.14);
        assertEquals(0,coverage.getHashLength());
    }

    @Test
    public void getHashLength_T2() {//測試陣列沒有元素應回傳0字元
        hashes.add("number1");
        hashes.add("number2");
        hashes.add("number3");
        hashes.add("number4");

        Coverage coverage=new Coverage(hashes,3.14);
        assertEquals(7,coverage.getHashLength());
    }
//------------------------------------------------------------------------------------------------------



}