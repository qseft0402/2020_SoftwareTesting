package com.github.davidmoten.geo.mem;

import com.google.common.base.Optional;
import com.google.common.collect.Lists;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.List;

import static org.junit.Assert.*;

public class GeomemTest {


    @Test
    public void find_OneItemInRange() {
        Geomem<String, String> g = new Geomem<String, String>();
        g.add(-20, 150, 5, "E2");
        List<Info<String, String>> list = Lists.newArrayList(g.find(0,
                100, -50, 200, 0, 10));
        assertEquals(1, list.size());
        assertEquals(-20, list.get(0).lat(), 0.0001);
        assertEquals(150, list.get(0).lon(), 0.0001);
        assertEquals((long)5, list.get(0).time());
        assertEquals("E2", list.get(0).value());
    }

}