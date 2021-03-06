from hl7trans import *
import compositetrans
transforms = {\
    'GT1': {\
        'set_id': (1, None),
        'guarantor_number': (2, None),
        'guarantor_name': (3, compositetrans.fieldtransformPN),
        'guarantor_spouse_name': (4, compositetrans.fieldtransformPN),
        'guarantor_address': (5, compositetrans.fieldtransformAD),
        'guarantor_phone_home': (6, None),
        'guarantor_phone_business': (7, None),
        'guarantor_date_of_birth': (8, datetransform),
        'guarantor_sex': (9, None),
        'guarantor_type': (10, None),
        'guarantor_relationship': (11, None),
        'guarantor_ssn': (12, None),
        'guarantor_date_begin': (13, datetransform),
        'guarantor_date_end': (14, datetransform),
        'guarantor_priority': (15, numtransform),
        'guarantor_employer_name': (16, None),
        'guarantor_employer_addr': (17, compositetrans.fieldtransformAD),
        'guarantor_employer_phone': (18, None),
        'guarantor_employee_id_num': (19, None),
        'guarantor_employmt_status': (20, None),
},
    'FHS': {\
        'file_field_separators': (1, None),
        'file_encoding_characters': (2, None),
        'file_sending_application': (3, None),
        'file_sending_facility': (4, None),
        'file_rcving_application': (5, None),
        'file_receiving_facility': (6, None),
        'file_creation_datetime': (7, datetransform),
        'file_security': (8, None),
        'file_nameidtype': (9, None),
        'file_comment': (10, None),
        'file_control_id': (11, None),
        'reference_file_cntrl_id': (12, None),
},
    'RX1': {\
        'unused': (1, compositetrans.fieldtransformUN),
        'unused': (2, compositetrans.fieldtransformUN),
        'route': (3, None),
        'site_administered': (4, None),
        'iv_solution_rate': (5, compositetrans.fieldtransformCQ),
        'drug_strength': (6, compositetrans.fieldtransformCQ),
        'final_concentration': (7, numtransform),
        'final_volume_in_ml': (8, numtransform),
        'drug_dose': (9, compositetrans.fieldtransformCM),
        'drug_role': (10, None),
        'prescription_sequence_num': (11, numtransform),
        'quantity_dispensed': (12, compositetrans.fieldtransformCQ),
        'unused': (13, compositetrans.fieldtransformUN),
        'drug_id': (14, compositetrans.fieldtransformCE),
        'component_drug_ids': (15, None),
        'prescription_type': (16, None),
        'substitution_status': (17, None),
        'rx_order_status': (18, None),
        'number_of_refills': (19, numtransform),
        'unused': (20, compositetrans.fieldtransformUN),
        'refills_remaining': (21, numtransform),
        'dea_class': (22, None),
        'ordering_mds_dea_number': (23, numtransform),
        'unused': (24, compositetrans.fieldtransformUN),
        'last_refill_datetime': (25, datetransform),
        'rx_number': (26, None),
        'prn_status': (27, None),
        'pharmacy_instructions': (28, None),
        'patient_instruction': (29, None),
        'instructions_sig': (30, None),
},
    'OBX': {\
        'set_id': (1, None),
        'value_type': (2, None),
        'observation_identifier': (3, compositetrans.fieldtransformCE),
        'observation_sub_id': (4, None),
        'observation_results': (5, None),
        'units': (6, None),
        'reference_range': (7, None),
        'abnormal_flags': (8, None),
        'probability': (9, numtransform),
        'nature_of_abnormal_test': (10, None),
        'observ_result_status': (11, None),
        'date_last_normal_value': (12, datetransform),
},
    'QRF': {\
        'where_subject_filter': (1, None),
        'when_data_start_datetime': (2, datetransform),
        'when_data_end_datetime': (3, datetransform),
        'what_user_qualifier': (4, None),
        'other_qry_subject_filter': (5, None),
},
    'DSC': {\
        'continuation_pointer': (1, None),
},
    'PID': {\
        'set_id': (1, None),
        'patient_id_external_id': (2, compositetrans.fieldtransformCK),
        'patient_id_internal_id': (3, compositetrans.fieldtransformCK),
        'alternate_patient_id': (4, None),
        'patients_name': (5, compositetrans.fieldtransformPN),
        'mothers_maiden_name': (6, None),
        'date_of_birth': (7, datetransform),
        'sex': (8, None),
        'patient_alias': (9, compositetrans.fieldtransformPN),
        'ethnic_group': (10, None),
        'patient_address': (11, compositetrans.fieldtransformAD),
        'county_code': (12, None),
        'phone_number_home': (13, None),
        'phone_number_business': (14, None),
        'language_patient': (15, None),
        'marital_status': (16, None),
        'religion': (17, None),
        'patient_account_number': (18, compositetrans.fieldtransformCK),
        'ssn_number_patient': (19, None),
        'drivers_license_patient': (20, compositetrans.fieldtransformCM),
},
    'ACC': {\
        'accident_datetime': (1, datetransform),
        'accident_code': (2, None),
        'accident_location': (3, None),
},
    'EVN': {\
        'event_type_code': (1, None),
        'datetime_of_event': (2, datetransform),
        'datetime_planned_event': (3, datetransform),
        'event_reason_code': (4, None),
},
    'NTE': {\
        'set_id': (1, None),
        'source_of_comment': (2, None),
        'comment': (3, None),
},
    'MRG': {\
        'prior_patient_id_internal': (1, compositetrans.fieldtransformCK),
        'prior_alt_patient_id': (2, compositetrans.fieldtransformCK),
        'prior_patient_account_num': (3, None),
},
    'DSP': {\
        'set_id': (1, None),
        'display_level': (2, None),
        'data_line': (3, None),
        'logical_break_point': (4, None),
        'result_id': (5, None),
},
    'UB1': {\
        'set_id': (1, None),
        'blood_deductible': (2, None),
        'blood_furn_pints_of_40': (3, None),
        'blook_replaced_pints_41': (4, None),
        'blood_not_rplcd_pints42': (5, None),
        'co_insurance_days_25': (6, None),
        'condition_code': (7, None),
        'covered_days_23': (8, None),
        'non_covered_days_24': (9, None),
        'value_amount_code': (10, compositetrans.fieldtransformCM),
        'number_of_grace_days_90': (11, None),
        'spec_prog_indicator44': (12, None),
        'psrour_approvl_ind_87': (13, None),
        'psrour_aprvd_stay_fm88': (14, datetransform),
        'psrour_aprvd_stay_to89': (15, datetransform),
        'occurrence_28_32': (16, None),
        'occurrence_span_33': (17, None),
        'occur_span_start_date33': (18, datetransform),
        'occur_span_end_date_33': (19, datetransform),
        'ub_82_locator_2': (20, None),
        'ub_82_locator_9': (21, None),
        'ub_82_locator_27': (22, None),
        'ub_82_locator_45': (23, None),
},
    'MSH': {\
        'field_separator': (0, None),
        'encoding_characters': (1, None),
        'sending_application': (2, None),
        'sending_facility': (3, None),
        'receiving_application': (4, None),
        'receiving_facility': (5, None),
        'datetime_of_message': (6, datetransform),
        'security': (7, None),
        'message_type': (8, compositetrans.fieldtransformCM),
        'message_control_id': (9, None),
        'processing_id': (10, None),
        'version_id': (11, numtransform),
        'sequence_number': (12, numtransform),
        'continuation_pointer': (13, None),
},
    'BHS': {\
        'batch_field_separator': (1, None),
        'batch_encoding_characters': (2, None),
        'batch_sending_application': (3, None),
        'batch_sending_facility': (4, None),
        'batch_rcving_application': (5, None),
        'batch_receiving_facility': (6, None),
        'batch_creation_datetime': (7, datetransform),
        'batch_security': (8, None),
        'batch_nameidtype': (9, None),
        'batch_comment': (10, None),
        'batch_control_id': (11, None),
        'reference_batch_cntrl_id': (12, None),
},
    'PV1': {\
        'set_id': (1, None),
        'patient_class': (2, None),
        'assigned_patient_location': (3, None),
        'admission_type': (4, None),
        'pre_admit_number': (5, None),
        'prior_patient_location': (6, None),
        'attending_doctor': (7, compositetrans.fieldtransformCN),
        'refering_doctor': (8, compositetrans.fieldtransformCN),
        'consulting_doctor': (9, compositetrans.fieldtransformCN),
        'hospital_service': (10, None),
        'temporary_location': (11, None),
        'pre_admit_test_indicator': (12, None),
        're_admission_indicator': (13, None),
        'admit_source': (14, None),
        'ambulatory_status': (15, None),
        'vip_indicators': (16, None),
        'admitting_doctor': (17, compositetrans.fieldtransformCN),
        'patient_type': (18, None),
        'visit_number': (19, numtransform),
        'financial_class': (20, None),
        'charge_price_indicator': (21, None),
        'courtesy_code': (22, None),
        'credit_rating': (23, None),
        'contract_code': (24, None),
        'contract_effective_date': (25, datetransform),
        'contract_amount': (26, numtransform),
        'contract_period': (27, numtransform),
        'interest_code': (28, None),
        'transfer_to_bad_debt_code': (29, None),
        'transfer_to_bad_debt_date': (30, datetransform),
        'bad_debt_agency_code': (31, None),
        'bad_debt_transfer_amount': (32, numtransform),
        'bad_debt_recovery_amount': (33, numtransform),
        'delete_account_indicator': (34, None),
        'delete_account_date': (35, datetransform),
        'discharge_disposition': (36, None),
        'discharged_to_location': (37, None),
        'diet_type': (38, None),
        'servicing_facility': (39, None),
        'bed_status': (40, None),
        'account_status': (41, None),
        'pending_location': (42, None),
        'prior_temporary_location': (43, None),
        'admit_datetime': (44, datetransform),
        'discharge_datetime': (45, datetransform),
        'current_patient_balance': (46, numtransform),
        'total_charges': (47, numtransform),
        'total_adjustments': (48, numtransform),
        'total_payments': (49, numtransform),
},
    'NPU': {\
        'bed_location': (1, None),
        'bed_status': (2, None),
},
    'BTS': {\
        'batch_message_count': (1, None),
        'batch_comment': (2, None),
        'batch_totals': (3, compositetrans.fieldtransformCM),
},
    'OBR': {\
        'set_id': (1, None),
        'placer_orders_num': (2, compositetrans.fieldtransformCM),
        'fillers_order_num': (3, compositetrans.fieldtransformCM),
        'universal_service_id': (4, compositetrans.fieldtransformCE),
        'priority': (5, None),
        'requested_datetime': (6, datetransform),
        'observation_datetime': (7, datetransform),
        'observation_end_datetime': (8, datetransform),
        'collection_volume': (9, compositetrans.fieldtransformCQ),
        'collector_identifier': (10, compositetrans.fieldtransformCN),
        'specimen_action_code': (11, None),
        'danger_code': (12, compositetrans.fieldtransformCM),
        'relevant_clinical_info': (13, None),
        'specimen_rcvd_datetime': (14, datetransform),
        'specimen_source': (15, compositetrans.fieldtransformCM),
        'ordering_provider': (16, compositetrans.fieldtransformCN),
        'order_call_back_phone_num': (17, None),
        'placers_field_num1': (18, None),
        'placers_field_num2': (19, None),
        'fillers_field_num1': (20, None),
        'fillers_field_num2': (21, None),
        'results_rptstatus_chg_dt': (22, datetransform),
        'charge_to_practice': (23, compositetrans.fieldtransformCM),
        'diagnostic_serv_sect_id': (24, None),
        'result_status': (25, None),
        'linked_results': (26, compositetrans.fieldtransformCE),
        'quantitytiming': (27, compositetrans.fieldtransformCM),
        'result_copies_to': (28, compositetrans.fieldtransformCN),
        'parent_accession_num': (29, compositetrans.fieldtransformCM),
        'transportation_mode': (30, None),
        'reason_for_study': (31, compositetrans.fieldtransformCE),
        'prin_result_interpreter': (32, compositetrans.fieldtransformCN),
        'asst_result_interpreter': (33, compositetrans.fieldtransformCN),
        'technician': (34, compositetrans.fieldtransformCN),
        'transcriptionist': (35, compositetrans.fieldtransformCN),
        'scheduled_datetime': (36, datetransform),
},
    'PR1': {\
        'set_id': (1, None),
        'procedure_coding_method': (2, None),
        'procedure_code': (3, None),
        'procedure_description': (4, None),
        'procedure_datetime': (5, datetransform),
        'procedure_type': (6, None),
        'procedure_minutes': (7, numtransform),
        'anesthesiologist': (8, compositetrans.fieldtransformCN),
        'anesthesia_code': (9, None),
        'anesthesia_minutes': (10, numtransform),
        'surgeon': (11, compositetrans.fieldtransformCN),
        'resident_code': (12, compositetrans.fieldtransformCN),
        'consent_code': (13, None),
},
    'FTS': {\
        'file_batch_count': (1, None),
        'file_trailer_comment': (2, compositetrans.fieldtransformCM),
},
    'URD': {\
        'ru_datetime': (1, None),
        'report_priority': (2, compositetrans.fieldtransformCK),
        'ru_who_subject_defnition': (3, compositetrans.fieldtransformCK),
        'ru_what_subject_defntion': (4, None),
        'ru_what_department_code': (5, compositetrans.fieldtransformPN),
        'ru_displayprint_locs': (6, None),
        'ru_results_level': (7, datetransform),
},
    'URS': {\
        'ru_where_subject_def': (1, None),
        'ru_when_start_dtetme': (2, datetransform),
        'ru_when_end_dtetme': (3, datetransform),
        'ru_what_user_qualifier': (4, None),
        'ru_oth_results_def': (5, None),
},
    'BLG': {\
        'when_to_charge': (1, compositetrans.fieldtransformCM),
        'value_type': (2, compositetrans.fieldtransformCM),
        'observation_identifier': (3, compositetrans.fieldtransformCM),
},
    'ORO': {\
        'order_item_id': (1, compositetrans.fieldtransformCE),
        'substitute_allowed': (2, None),
        'results_copied_to': (3, compositetrans.fieldtransformCN),
        'stock_location': (4, None),
},
    'ORC': {\
        'order_control': (1, None),
        'placer_order_num': (2, compositetrans.fieldtransformCM),
        'filler_order_num': (3, compositetrans.fieldtransformCM),
        'placer_order_num': (4, compositetrans.fieldtransformCM),
        'order_status': (5, None),
        'response_flag': (6, None),
        'timingquantity': (7, compositetrans.fieldtransformCM),
        'parent': (8, compositetrans.fieldtransformCM),
        'datetime_of_transaction': (9, datetransform),
        'entered_by': (10, compositetrans.fieldtransformCN),
        'verified_by': (11, compositetrans.fieldtransformCN),
        'ordering_provider': (12, compositetrans.fieldtransformCN),
        'enterers_location': (13, compositetrans.fieldtransformCM),
        'call_back_phone_number': (14, None),
},
    'FT1': {\
        'set_id': (1, None),
        'transaction_id': (2, None),
        'transaction_batch_id': (3, None),
        'transaction_date': (4, datetransform),
        'transaction_posting_date': (5, datetransform),
        'transaction_type': (6, None),
        'transaction_code': (7, None),
        'transaction_description': (8, None),
        'transaction_description_alternative': (9, None),
        'transaction_quantity': (10, numtransform),
        'transaction_amount_ext': (11, numtransform),
        'transaction_amount_unit': (12, numtransform),
        'department_code': (13, None),
        'insurance_plan_id': (14, None),
        'insurance_amount': (15, numtransform),
        'patient_location': (16, None),
        'fee_schedule': (17, None),
        'patient_type': (18, None),
        'diagnosis_code': (19, None),
        'performed_by_code': (20, compositetrans.fieldtransformCN),
        'ordered_by_code': (21, compositetrans.fieldtransformCN),
        'unit_cost': (22, numtransform),
},
    'NK1': {\
        'set_id': (1, None),
        'next_of_kin_name': (2, compositetrans.fieldtransformPN),
        'next_of_kin_relationship': (3, None),
        'next_of_kin_address': (4, compositetrans.fieldtransformAD),
        'next_of_kin_phone_number': (5, None),
},
    'DG1': {\
        'set_id': (1, None),
        'diagnosis_coding_method': (2, None),
        'diagnosis_code': (3, None),
        'diagnosis_description': (4, None),
        'diagnosis_datetime': (5, datetransform),
        'diagnosisdrg_type': (6, None),
        'major_diagnostic_category': (7, None),
        'diagnostic_related_group': (8, None),
        'drg_approval_indicator': (9, None),
        'drg_grouper_review_code': (10, None),
        'outlier_type': (11, None),
        'outlier_days': (12, numtransform),
        'outlier_cost': (13, numtransform),
        'grouper_version_and_type': (14, None),
},
    'ERR': {\
        'error_code_and_location': (1, None),
},
    'QRD': {\
        'query_datetime': (1, datetransform),
        'query_format_code': (2, None),
        'query_priority': (3, None),
        'query_id': (4, None),
        'deferred_response_type': (5, None),
        'def_resp_datetime': (6, datetransform),
        'quantity_limited_request': (7, compositetrans.fieldtransformCQ),
        'who_subject_filter': (8, None),
        'what_subject_filter': (9, None),
        'what_dept_data_code': (10, None),
        'what_data_cd_value_qua': (11, None),
        'query_results_level': (12, None),
},
    'ADD': {\
        '1': (1, None),
},
    'IN1': {\
        'set_id': (1, None),
        'insurance_plan_id': (2, None),
        'insurance_company_id': (3, None),
        'insurance_company_name': (4, None),
        'insurance_company_address': (5, compositetrans.fieldtransformAD),
        'insurance_co_contact_pers': (6, compositetrans.fieldtransformPN),
        'insurance_co_phone_number': (7, None),
        'group_number': (8, None),
        'group_name': (9, None),
        'insureds_group_emp_id': (10, None),
        'insureds_group_emp_name': (11, None),
        'plan_effective_date': (12, datetransform),
        'plan_expiration_date': (13, datetransform),
        'authorization_information': (14, None),
        'plan_type': (15, None),
        'name_of_insured': (16, compositetrans.fieldtransformPN),
        'insureds_relation_to_pat': (17, None),
        'insureds_date_of_birth': (18, datetransform),
        'insureds_address': (19, compositetrans.fieldtransformAD),
        'assignment_of_benefits': (20, None),
        'coordination_of_benefits': (21, None),
        'coord_of_ben_priority': (22, None),
        'notice_of_admission_code': (23, None),
        'notice_of_admission_date': (24, datetransform),
        'rpt_of_eligibility_code': (25, None),
        'rpt_of_eligibility_date': (26, datetransform),
        'release_information_code': (27, None),
        'pre_admit_cert_pac': (28, None),
        'verification_date': (29, datetransform),
        'verification_by': (30, compositetrans.fieldtransformCM),
        'type_of_agreement_code': (31, None),
        'billing_status': (32, None),
        'lifetime_reserve_days': (33, numtransform),
        'delay_before_l_r_day': (34, numtransform),
        'company_plan_code': (35, None),
        'policy_number': (36, None),
        'policy_deductible': (37, numtransform),
        'policy_limit_amount': (38, numtransform),
        'policy_limit_days': (39, numtransform),
        'room_rate_semi_private': (40, numtransform),
        'room_rate_private': (41, numtransform),
        'insureds_employ_status': (42, None),
        'insureds_sex': (43, None),
        'insureds_employer_addresss': (44, compositetrans.fieldtransformAD),
},
    'MSA': {\
        'acknowledgement_code': (1, None),
        'message_control_id': (2, None),
        'text_message': (3, None),
        'expected_sequence_number': (4, numtransform),
        'delayed_ack_type': (5, None),
},
}
