package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class LatLongTest {

    LatLong latLong;
    @Before
    public void setUp() throws Exception {
        latLong=new LatLong(3.123,4.123);
    }

    @After
    public void tearDown() throws Exception {
        latLong=null;
        assertNull(latLong);
    }

    @Test
    public void testGetLat() {
        assertEquals(3.123,latLong.getLat(),0.00001);
    }

    @Test
    public void testGetLon() {
        assertEquals(4.123,latLong.getLon(),0.00001);

    }

    @Test
    public void testAdd() {
        LatLong latLong1=latLong.add(3,3);
        assertEquals(3.123,latLong.getLat(),0.00001);
        assertEquals(4.123,latLong.getLon(),0.00001);
        assertEquals(6.123,latLong1.getLat(),0.00001);
        assertEquals(7.123,latLong1.getLon(),0.00001);
    }

    @Test
    public void testToString1() {
        assertEquals("LatLong [lat=3.123, lon=4.123]",latLong.toString());
    }
}