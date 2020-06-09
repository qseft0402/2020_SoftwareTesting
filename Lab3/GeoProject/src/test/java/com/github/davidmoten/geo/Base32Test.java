package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;


import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;

public class Base32Test {

//------------------------------------------------------------------------------------------------------
    @Test
    public void encodeBase32_T1() throws Exception {//測試10進制轉32進制
        String encode = Base32.encodeBase32(-75324, -4);
        assertEquals("-29jw", encode);
    }
    @Test
    public void encodeBase32_T2() throws Exception {//測試10進制轉32進制
        String encode = Base32.encodeBase32(-75324, 0);
        assertEquals("-29jw", encode);
    }
    @Test
    public void encodeBase32_T3() throws Exception {//測試10進制轉32進制
        String encode = Base32.encodeBase32(-75324, 4);
        assertEquals("-29jw", encode);
    }


    @Test
    public void encodeBase32_T4() throws Exception {//測試10進制轉32進制
        String encode = Base32.encodeBase32(0, -4);
        assertEquals("0", encode);
    }
    @Test
    public void encodeBase32_T5() throws Exception {//測試10進制轉32進制
        String encode = Base32.encodeBase32(0, 0);
        assertEquals("0", encode);
    }
    @Test
    public void encodeBase32_T6() throws Exception {//測試10進制轉32進制
        String encode = Base32.encodeBase32(0, 4);
        assertEquals("0000", encode);
    }


    @Test
    public void encodeBase32_T7() throws Exception {//測試10進制轉32進制
        String encode = Base32.encodeBase32(75324, -4);
        assertEquals("29jw", encode);
    }
    @Test
    public void encodeBase32_T8() throws Exception {//測試10進制轉32進制
        String encode = Base32.encodeBase32(75324, 0);
        assertEquals("29jw", encode);
    }
    @Test
    public void encodeBase32_T9() throws Exception {//測試10進制轉32進制
        String encode = Base32.encodeBase32(75324, 4);
        assertEquals("29jw", encode);
    }
//------------------------------------------------------------------------------------------------------

    @Test
    public void encodeBase32_noLength_positive_T1() throws Exception {//10進制轉32進制 測試單一參數
        String encode = Base32.encodeBase32(-75324);
        assertEquals("-0000000029jw", encode);
    }
    @Test
    public void encodeBase32_noLength_zero_T2() throws Exception {//10進制轉32進制 測試單一參數
        String encode = Base32.encodeBase32(0);
        assertEquals("000000000000", encode);
    }
    @Test
    public void encodeBase32_noLength_negative_T3() throws Exception {//10進制轉32進制 測試單一參數
        String encode = Base32.encodeBase32(75324);
        assertEquals("0000000029jw", encode);
    }
    //------------------------------------------------------------------------------------------------------

    @Test//**
    public void decodeBase32_positive_T1() throws Exception {//測試正數 32進制轉10進制
        long dencode = Base32.decodeBase32("29jw");
        assertEquals(75324, dencode);
    }
    @Test //**
    public void decodeBase32_zero_T2() throws Exception {//測試0 32進制轉10進制
        long dencode = Base32.decodeBase32("0");
        assertEquals(0, dencode);
    }
    @Test  //**
    public void decodeBase32_negative_T3() throws Exception {//測試負數 32進制轉10進制
        long dencode = Base32.decodeBase32("-29jw");
        assertEquals(-75324, dencode);
    }

//------------------------------------------------------------------------------------------------------

    @Test
    public void getCharIndex_exception_T1() throws Exception {//測試當'b' 回傳為11
        try{
            int index = Base32.getCharIndex('b');
            assertEquals(10,index);
        }catch(IllegalArgumentException e){
            assertTrue(false);
        }

    }

    @Test
    public void getCharIndex_exception_T2() throws Exception {//測試當'i'不再編碼中的拋出例外
        try{
            int index = Base32.getCharIndex('i');

        }catch(IllegalArgumentException e){
            assertTrue(true);
            return;
        }
        fail("IllegalArgumentException no throw");
    }

//------------------------------------------------------------------------------------------------------

    @Test
    public void getCharIndex_padLeftWithZerosToLength_T1() throws Exception {//測試補0功能
        String index = Base32.padLeftWithZerosToLength("-29jw",-5);
        assertEquals("-29jw",index);
    }
    @Test
    public void getCharIndex_padLeftWithZerosToLength_T2() throws Exception {//測試補0功能
        String index = Base32.padLeftWithZerosToLength("-29jw",0);
        assertEquals("-29jw",index);
    }
    @Test
    public void getCharIndex_padLeftWithZerosToLength_T3() throws Exception {//測試補0功能
        String index = Base32.padLeftWithZerosToLength("-29jw",5);
        assertEquals("-29jw",index);
    }


    @Test
    public void getCharIndex_padLeftWithZerosToLength_T4() throws Exception {//測試補0功能
        String index = Base32.padLeftWithZerosToLength("0",-5);
        assertEquals("0",index);
    }
    @Test
    public void getCharIndex_padLeftWithZerosToLength_T5() throws Exception {//測試補0功能
        String index = Base32.padLeftWithZerosToLength("0",0);
        assertEquals("0",index);
    }
    @Test
    public void getCharIndex_padLeftWithZerosToLength_T6() throws Exception {//測試補0功能
        String index = Base32.padLeftWithZerosToLength("0",5);
        assertEquals("00000",index);
    }


    @Test
    public void getCharIndex_padLeftWithZerosToLength_T7() throws Exception {//測試補0功能
        String index = Base32.padLeftWithZerosToLength("29jw",-5);
        assertEquals("29jw",index);
    }
    @Test
    public void getCharIndex_padLeftWithZerosToLength_T8() throws Exception {//測試補0功能
        String index = Base32.padLeftWithZerosToLength("29jw",0);
        assertEquals("29jw",index);
    }
    @Test
    public void getCharIndex_padLeftWithZerosToLength_T9() throws Exception {//測試補0功能
        String index = Base32.padLeftWithZerosToLength("29jw",5);
        assertEquals("029jw",index);
    }
//------------------------------------------------------------------------------------------------------
    @Test
    public void decodeBase32_CFG_P1() throws Exception {
        try {
            Base32.decodeBase32("-a");
            assertTrue(false);
        }catch (IllegalArgumentException e){
            assertTrue(true);
        }
    }
    @Test
    public void decodeBase32_CFG_P2() throws Exception {
        long dencode = Base32.decodeBase32("-b");
        assertEquals(-10, dencode);
    }
    @Test
    public void decodeBase32_CFG_P3() throws Exception {
        long dencode = Base32.decodeBase32("-c");
        assertEquals(-11, dencode);
    }

    @Test
    public void decodeBase32_CFG_P4() throws Exception {
        try {
            long dencode = Base32.decodeBase32("a");
            assertTrue(false);
        }catch (IllegalArgumentException e){
            assertTrue(true);
        }
    }
    @Test
    public void decodeBase32_CFG_P5() throws Exception {
        long dencode = Base32.decodeBase32("b");
        assertEquals(10, dencode);
    }
    @Test
    public void decodeBase32_CFG_P6() throws Exception {
        long dencode = Base32.decodeBase32("c");
        assertEquals(11, dencode);
    }

//------------------------------------------------------------------------------------------------------

    @Test
    public void encodeBase32_CFG_P1() throws Exception {
        String encode = Base32.encodeBase32(31, 4);
        assertEquals("000z", encode);
    }
    @Test
    public void encodeBase32_CFG_P2() throws Exception {
        String encode = Base32.encodeBase32(10, 4);
        assertEquals("000b", encode);
    }

    @Test
    public void encodeBase32_CFG_P3() throws Exception {
        String encode = Base32.encodeBase32(-31, 4);
        assertEquals("-000z", encode);
    }

    @Test
    public void encodeBase32_CFG_P4() throws Exception {
        String encode = Base32.encodeBase32(-10, 4);
        assertEquals("-000b", encode);
    }
//------------------------------------------------------------------------------------------------------

    @Test
    public void padLeftWithZerosToLength_CFG_P1(){//測試補0功能
        String index = Base32.padLeftWithZerosToLength("29jw",4);
        assertEquals("29jw", index);

    }
    @Test
    public void padLeftWithZerosToLength_CFG_P2(){//測試補0功能
        String index = Base32.padLeftWithZerosToLength("29jw",5);
        assertEquals("029jw", index);

    }
}