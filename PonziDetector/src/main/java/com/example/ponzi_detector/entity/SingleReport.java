package com.example.ponzi_detector.entity;

import javax.persistence.Entity;
import javax.persistence.Id;
import java.io.Serializable;

@Entity
public class SingleReport implements Serializable {

    public SingleReport() {};

    @Id
    private String address;
    private int isPozi;

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public int getIsPozi() {
        return isPozi;
    }

    public void setIsPozi(int isPozi) {
        this.isPozi = isPozi;
    }
}
