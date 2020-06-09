package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;


import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;

public class Base32Test {

    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void encodeBase32() throws Exception {//測試10進制轉32進制
        String encode = Base32.encodeBase32(75324, 4);
        assertEquals("29jw", encode);
    }

    @Test
    public void encodeBase32_negative() throws Exception {//測試10進制轉32進制
        String encode = Base32.encodeBase32(-75324, 4);
        assertEquals("-29jw", encode);
    }

    @Test
    public void encodeBase32_noLength() throws Exception {//10進制轉32進制 測試單一參數
        String encode = Base32.encodeBase32(75324);
        assertEquals("0000000029jw", encode);
    }
    @Test
    public void decodeBase32() throws Exception {//測試32進制轉10進制
        long dencode = Base32.decodeBase32("29jw");
        assertEquals(75324, dencode);
    }
    @Test
    public void decodeBase32_negative() throws Exception {//測試32進制轉10進制
        long dencode = Base32.decodeBase32("-29jw");
        assertEquals(-75324, dencode);
    }
    @Test
    public void getCharIndex() throws Exception {//測試'j'為編碼陣列中第幾個索引
        try {
            int index = Base32.getCharIndex('j');
            assertEquals(17, index);
        }catch(IllegalArgumentException e){
            assertTrue(false);
        }
    }


    @Test
    public void getCharIndex_exception() throws Exception {//測試當'i'不再編碼中的拋出例外
        try{
            int index = Base32.getCharIndex('i');

        }catch(IllegalArgumentException e){
            assertTrue(true);
            return;
        }
        fail("IllegalArgumentException no throw");
    }
    @Test
    public void getCharIndex_padLeftWithZerosToLength() throws Exception {//測試補0功能
        try{
            String index = Base32.padLeftWithZerosToLength("jw",6);
            assertEquals("0000jw",index);
        }catch(Exception e){
            fail("IllegalArgumentException throw");
        }
    }



//    @org.junit.Before
//    public void setUp() throws Exception {
//    }
//
//    @org.junit.After
//    public void tearDown() throws Exception {
//    }
}