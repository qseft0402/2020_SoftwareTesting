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
    public void id() {//測試回傳id是否與optional為同一記憶體位置
        assertEquals(optional,info.id());

    }

    @Test
    public void lat() {//測試回傳lat是否為當初設定的3.123
        assertEquals(3.123,info.lat(),0.00001);

    }

    @Test
    public void lon() {//測試回傳lon是否為當初設定的4.123
        assertEquals(4.123,info.lon(),0.00001);

    }

    @Test
    public void time() {//測試回傳time是否為當初設定的10
        assertEquals(10,info.time());

    }

    @Test
    public void value() {//測試回傳value是否為當初設定的5
        assertEquals(5,info.value());

    }

    @Test
    public void testToString() {//測試回傳string是否為正確資訊
        assertEquals("Info [lat=3.123, lon=4.123, time=10, value=5, id=Optional.of(NTUT)]",info.toString());
    }


}