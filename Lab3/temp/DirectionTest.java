package com.github.davidmoten.geo;

import org.junit.Test;


import static com.github.davidmoten.geo.Direction.*;
import static org.junit.Assert.*;

public class DirectionTest {

    @Test
    public void opposite() {//測試將陣列中的值轉為相反值回傳回來
        Direction[] dArr=Direction.values();
        assertEquals(dArr[0].opposite(),TOP);
        assertEquals(dArr[1].opposite(),BOTTOM);
        assertEquals(dArr[2].opposite(),RIGHT);
        assertEquals(dArr[3].opposite(),LEFT);

    }
}