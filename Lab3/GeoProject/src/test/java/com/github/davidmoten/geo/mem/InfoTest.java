package com.github.davidmoten.geo.mem;

import com.google.common.base.Optional;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import javax.swing.text.html.Option;

import static org.junit.Assert.*;

public class InfoTest {
    Info info;
    Optional<String> optional;
    @Before
    public void setUp() throws Exception {
        String name = "NTUT";
        optional = Optional.of(name);
        info=new Info(3.123,4.123,10, 5, optional);

    }

    @After
    public void tearDown() throws Exception {
        info=null;
        optional=null;
        assertNull(info);
        assertNull(optional);

    }
    @Test
    public void testToString() {//測試回傳string是否為正確資訊
        assertEquals("Info [lat=3.123, lon=4.123, time=10, value=5, id=Optional.of(NTUT)]",info.toString());
    }


}