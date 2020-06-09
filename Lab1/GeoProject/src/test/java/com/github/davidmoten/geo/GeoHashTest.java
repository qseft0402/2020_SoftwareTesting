package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.List;

import static org.junit.Assert.*;

public class GeoHashTest {

    @Test
    public void adjacentHash() {//km區域上面是kq
        String str=GeoHash.adjacentHash("km",Direction.TOP);
        assertEquals("kq",str);
    }
    @Test
    public void adjacentHash_steps() {//w往左五格是9
        String str=GeoHash.adjacentHash("w",Direction.LEFT,5);
        assertEquals("9",str);
    }
    @Test
    public void decodeHash() {//將geohash 0000轉為經緯度為-89.91210938及-179.82421875
        LatLong latLong=GeoHash.decodeHash("0000");
        assertEquals(latLong.getLat(),-89.91210938,0.00001);
        assertEquals(latLong.getLon(),-179.82421875,0.00001);
    }


    @Test
    public void encodeHash_lat_long() {//將經緯度-38.23242188, -149.58984375 轉換為geohash為29jw
        String geoHash=GeoHash.encodeHash(-38.23242188, -149.58984375,4);

        assertEquals("29jw",geoHash);
    }
    @Test
    public void left() {//測試w區域左邊(西邊)區域為t
        String geohash=GeoHash.left("w");

        assertEquals("t",geohash);
    }
    @Test
    public void right() {//測試w區域左邊(東邊)區域為x
        String geohash=GeoHash.right("w");

        assertEquals("x",geohash);
    }
    @Test
    public void top() {//測試w區域左邊(北邊)區域為y
        String geohash=GeoHash.top("w");

        assertEquals("y",geohash);
    }
    @Test
    public void bottom() {//測試w區域左邊(南邊)區域為q
        String geoHash=GeoHash.bottom("w");

        assertEquals("q",geoHash);
    }
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
    public void fromLongToString() {//測試當hash小於1將拋出例外
        long hash=-1;
        try {
            String geoHash = GeoHash.fromLongToString(hash);
        }catch (IllegalArgumentException e){

            assertEquals("invalid long geohash " + hash,e.getMessage());
        }

    }


    @Test
    public void hashLengthToCoverBoundingBox() {


        int num = GeoHash.hashLengthToCoverBoundingBox(1.123,2.123,3.123,4.123);
        assertEquals(2,num);
    }

    @Test
    public void hashContains() {//測試geohash wz是否再此經緯度參數區域內

        boolean isContain = GeoHash.hashContains("wz",42.18750000, 129.37500000);
        assertTrue(isContain);
    }

    @Test
    public void coverBoundingBoxLongs() {

        Coverage coverage = GeoHash.coverBoundingBox(42.18750000, 129.37500000,42.18750000, 129.37500000);
        assertEquals(12,coverage.getHashLength());

    }

}