package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static org.junit.Assert.*;

public class GeoHashTest {
//------------------------------------------------------------------------------------------------------

    @Test
    public void adjacentHash_T1() {//km區域上面是kq
        String str=GeoHash.adjacentHash("zz",Direction.TOP);
        assertEquals("gb",str);
    }
    @Test
    public void adjacentHash_T2() {//zz區域上面是zy
        String str=GeoHash.adjacentHash("zz",Direction.BOTTOM);
        assertEquals("zy",str);
    }
    @Test
    public void adjacentHash_T3() {//zz區域上面是zx
        String str=GeoHash.adjacentHash("zz",Direction.LEFT);
        assertEquals("zx",str);
    }
    @Test
    public void adjacentHash_T4() {//zz區域上面是bp
        String str=GeoHash.adjacentHash("zz",Direction.RIGHT);
        assertEquals("bp",str);
    }


    @Test
    public void adjacentHash_T5() {//ts區域上面是tt
        String str=GeoHash.adjacentHash("ts",Direction.TOP);
        assertEquals("tt",str);
    }   @Test
    public void adjacentHash_T6() {//ts區域上面是te
        String str=GeoHash.adjacentHash("ts",Direction.BOTTOM);
        assertEquals("te",str);
    }   @Test
    public void adjacentHash_T7() {//ts區域上面是tk
        String str=GeoHash.adjacentHash("ts",Direction.LEFT);
        assertEquals("tk",str);
    }   @Test
    public void adjacentHash_T8() {//ts區域上面是tu
        String str=GeoHash.adjacentHash("ts",Direction.RIGHT);
        assertEquals("tu",str);
    }

//------------------------------------------------------------------------------------------------------

    @Test
    public void adjacentHash_steps_T1() {//zz往左五格是-5
        String str=GeoHash.adjacentHash("zz",Direction.TOP,-5);
        assertEquals("zf",str);
    }
    @Test
    public void adjacentHash_steps_T2() {//zz往下-5格是qu
        String str=GeoHash.adjacentHash("zz",Direction.BOTTOM,-5);
        assertEquals("gu",str);
    }
    @Test
    public void adjacentHash_steps_T3() {//zz往左五格是-5
        String str=GeoHash.adjacentHash("zz",Direction.LEFT,-5);
        assertEquals("cp",str);
    }
    @Test
    public void adjacentHash_steps_T4() {//zz往左五格是5
        String str=GeoHash.adjacentHash("zz",Direction.RIGHT,-5);
        assertEquals("yx",str);
    }


    @Test
    public void adjacentHash_steps_T5() {//zz往左五格是5
        String str=GeoHash.adjacentHash("zz",Direction.TOP,0);
        assertEquals("zz",str);
    }
    @Test
    public void adjacentHash_steps_T6() {//zz往左五格是5
        String str=GeoHash.adjacentHash("zz",Direction.BOTTOM,0);
        assertEquals("zz",str);
    }
    @Test
    public void adjacentHash_steps_T7() {//zz往左五格是5
        String str=GeoHash.adjacentHash("zz",Direction.LEFT,0);
        assertEquals("zz",str);
    }
    @Test
    public void adjacentHash_steps_T8() {//zz往左五格是5
        String str=GeoHash.adjacentHash("zz",Direction.RIGHT,0);
        assertEquals("zz",str);
    }


    @Test
    public void adjacentHash_steps_T9() {//zz往左五格是5
        String str=GeoHash.adjacentHash("zz",Direction.TOP,5);
        assertEquals("gu",str);
    }
    @Test
    public void adjacentHash_steps_T10() {//zz往左五格是5
        String str=GeoHash.adjacentHash("zz",Direction.BOTTOM,5);
        assertEquals("zf",str);
    }
    @Test
    public void adjacentHash_steps_T11() {//zz往左五格是5
        String str=GeoHash.adjacentHash("zz",Direction.LEFT,5);
        assertEquals("yx",str);
    }
    @Test
    public void adjacentHash_steps_T12() {//zz往左五格是5
        String str=GeoHash.adjacentHash("zz",Direction.RIGHT,5);
        assertEquals("cp",str);
    }


    @Test
    public void adjacentHash_steps_T13() {//zz往左五格是5
        String str=GeoHash.adjacentHash("ts",Direction.TOP,-5);
        assertEquals("mx",str);
    }
    @Test
    public void adjacentHash_steps_T14() {//zz往左五格是5
        String str=GeoHash.adjacentHash("ts",Direction.BOTTOM,-5);
        assertEquals("v9",str);
    }
    @Test
    public void adjacentHash_steps_T15() {//zz往左五格是5
        String str=GeoHash.adjacentHash("ts",Direction.LEFT,-5);
        assertEquals("wu",str);
    }
    @Test
    public void adjacentHash_steps_T16() {//zz往左五格是5
        String str=GeoHash.adjacentHash("ts",Direction.RIGHT,-5);
        assertEquals("sk",str);
    }

    @Test
    public void adjacentHash_steps_T17() {//zz往左五格是5
        String str=GeoHash.adjacentHash("ts",Direction.TOP,0);
        assertEquals("ts",str);
    }
    @Test
    public void adjacentHash_steps_T18() {//zz往左五格是5
        String str=GeoHash.adjacentHash("ts",Direction.BOTTOM,0);
        assertEquals("ts",str);
    }
    @Test
    public void adjacentHash_steps_T19() {//zz往左五格是5
        String str=GeoHash.adjacentHash("ts",Direction.LEFT,0);
        assertEquals("ts",str);
    }
    @Test
    public void adjacentHash_steps_T20() {//zz往左五格是5
        String str=GeoHash.adjacentHash("ts",Direction.RIGHT,0);
        assertEquals("ts",str);
    }

    @Test
    public void adjacentHash_steps_T21() {//zz往左五格是5
        String str=GeoHash.adjacentHash("ts",Direction.TOP,5);
        assertEquals("v9",str);
    }
    @Test
    public void adjacentHash_steps_T22() {//zz往左五格是5
        String str=GeoHash.adjacentHash("ts",Direction.BOTTOM,5);
        assertEquals("mx",str);
    }
    @Test
    public void adjacentHash_steps_T23() {//zz往左五格是5
        String str=GeoHash.adjacentHash("ts",Direction.LEFT,5);
        assertEquals("sk",str);
    }
    @Test
    public void adjacentHash_steps_T24() {//zz往左五格是5
        String str = GeoHash.adjacentHash("ts", Direction.RIGHT, 5);
        assertEquals("wu", str);
    }
//------------------------------------------------------------------------------------------------------

    @Test
    public void decodeHash_T1() {//將geohash 0000轉為經緯度為-89.91210938及-179.82421875
        LatLong latLong=GeoHash.decodeHash("-sb52");
        assertEquals(72.31201171875,latLong.getLat(),0.00001);
        assertEquals(157.52197265625,latLong.getLon(),0.00001);
    }
    @Test
    public void decodeHash_T2() {//將geohash 0000轉為經緯度為-89.91210938及-179.82421875
        LatLong latLong=GeoHash.decodeHash("0");
        assertEquals(-67.5,latLong.getLat(),0.00001);
        assertEquals(-157.5,latLong.getLon(),0.00001);
    }
    @Test
    public void decodeHash_T3() {//將geohash 0000轉為經緯度為-89.91210938及-179.82421875
        LatLong latLong=GeoHash.decodeHash("sb52");
        assertEquals(0.087890625,latLong.getLat(),0.00001);
        assertEquals(38.49609375,latLong.getLon(),0.00001);
    }
//------------------------------------------------------------------------------------------------------

    @Test
    public void right_T1() {
        String answer=GeoHash.right("zz");
        assertEquals("bp",answer);
    }
    @Test
    public void right_T2() {
        String answer=GeoHash.right("ts");
        assertEquals("tu",answer);
    }
    @Test
    public void left_T1() {
        String answer=GeoHash.left("zz");
        assertEquals("zx",answer);
    }
    @Test
    public void left_T2() {
        String answer=GeoHash.left("ts");
        assertEquals("tk",answer);
    }
    @Test
    public void top_T1() {
        String answer=GeoHash. top("zz");
        assertEquals("gb",answer);
    }
    @Test
    public void top_T2() {
        String answer=GeoHash. top("ts");
        assertEquals("tt",answer);
    }
    @Test
    public void bottom_T1() {
        String answer=GeoHash.bottom("zz");
        assertEquals("zy",answer);
    }
    @Test
    public void bottom_T2() {
        String answer=GeoHash.bottom("ts");
        assertEquals("te",answer);
    }

//------------------------------------------------------------------------------------------------------



    @Test
    public void neighbours() {//測試w區域八方位的geohash
        List<String> geohash=GeoHash.neighbours("w");

        assertEquals("t",geohash.get(0));
        assertEquals("x",geohash.get(1));
        assertEquals("y",geohash.get(2));
        assertEquals("q",geohash.get(3));
        assertEquals("v",geohash.get(4));
        assertEquals("m",geohash.get(5));
        assertEquals("z",geohash.get(6));
        assertEquals("r",geohash.get(7));

    }


    @Test
    public void gridAsString() {
        HashSet<String> set=new HashSet<String>();
        set.add("tt");
        set.add("tk");
        set.add("te");

        String str=GeoHash.gridAsString("ts",-1,set);
        System.out.println(str);
    }
}