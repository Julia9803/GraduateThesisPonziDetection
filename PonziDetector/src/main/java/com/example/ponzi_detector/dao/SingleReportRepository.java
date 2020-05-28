package com.example.ponzi_detector.dao;

import com.example.ponzi_detector.entity.SingleReport;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SingleReportRepository extends CrudRepository<SingleReport,String> {
    SingleReport getByAddress(String address);
}
