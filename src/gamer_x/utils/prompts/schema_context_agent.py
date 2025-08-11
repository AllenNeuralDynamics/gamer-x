import json
def get_schema_context_prompt(query: str,
                              schema_context:str,
                              tool_call_count:int):
    
    sample_acquisition = json.dumps(
        {"acquisition": {
            "active_objectives": None,
            "axes": [
            {
                "dimension": 2,
                "direction": "Left_to_right",
                "name": "X",
                "unit": "micrometer"
            },
            {
                "dimension": 1,
                "direction": "Posterior_to_anterior",
                "name": "Y",
                "unit": "micrometer"
            },
            {
                "dimension": 0,
                "direction": "Superior_to_inferior",
                "name": "Z",
                "unit": "micrometer"
            }
            ],
            "chamber_immersion": {
            "medium": "Cargille oil",
            "refractive_index": 1.5208
            },
            "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/imaging/acquisition.py",
            "experimenter_full_name": "John Rohde",
            "external_storage_directory": "",
            "instrument_id": "SmartSPIM1-1",
            "local_storage_directory": "D:",
            "sample_immersion": None,
            "schema_version": "0.4.2",
            "session_end_time": "2023-03-06T22:59:16",
            "session_start_time": "2023-03-06T17:47:13",
            "specimen_id": "",
            "subject_id": "662616",
            "tiles": [
            {
                "channel": {
                "channel_name": "488.0",
                "filter_wheel_index": 1,
                "laser_power": 20,
                "laser_power_unit": "milliwatt",
                "laser_wavelength": 488,
                "laser_wavelength_unit": "nanometer"
                },
                "coordinate_transformations": [
                {
                    "translation": [
                    42033,
                    41585,
                    10.8
                    ],
                    "type": "translation"
                },
                {
                    "scale": [
                    1.8,
                    1.8,
                    2
                    ],
                    "type": "scale"
                }
                ],
                "file_name": "Ex_488_Em_525/420330/420330_415850/",
                "imaging_angle": 0,
                "imaging_angle_unit": "degree",
                "notes": "\nLaser power is in percentage of total -- needs calibration"
            },
            {
                "channel": {
                "channel_name": "445.0",
                "filter_wheel_index": 0,
                "laser_power": 30,
                "laser_power_unit": "milliwatt",
                "laser_wavelength": 445,
                "laser_wavelength_unit": "nanometer"
                },
                "coordinate_transformations": [
                {
                    "translation": [
                    45273,
                    41585,
                    10.8
                    ],
                    "type": "translation"
                },
                {
                    "scale": [
                    1.8,
                    1.8,
                    2
                    ],
                    "type": "scale"
                }
                ],
                "file_name": "Ex_445_Em_469/452730/452730_415850/",
                "imaging_angle": 0,
                "imaging_angle_unit": "degree",
                "notes": "\nLaser power is in percentage of total -- needs calibration"
            }
            ]
        }}
    )

    sample_data_description = json.dumps(
        {
            "data_description": {
                "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/core/data_description.py",
                "schema_version": "1.0.0",
                "license": "CC-BY-4.0",
                "platform": {
                "name": "SmartSPIM platform",
                "abbreviation": "SmartSPIM"
                },
                "subject_id": "662616",
                "creation_time": "2023-04-14T15:11:04-07:00",
                "label": None,
                "name": "SmartSPIM_662616_2023-04-14_15-11-04",
                "institution": {
                "name": "Allen Institute for Neural Dynamics",
                "abbreviation": "AIND",
                "registry": {
                    "name": "Research Organization Registry",
                    "abbreviation": "ROR"
                },
                "registry_identifier": "04szwah67"
                },
                "funding_source": [
                {
                    "funder": {
                    "name": "National Institute of Neurological Disorders and Stroke",
                    "abbreviation": "NINDS",
                    "registry": {
                        "name": "Research Organization Registry",
                        "abbreviation": "ROR"
                    },
                    "registry_identifier": "01s5ya894"
                    },
                    "grant_number": "NIH1U19NS123714-01",
                    "fundee": "Jayaram Chandreashekar, Mathew Summers"
                }
                ],
                "data_level": "raw",
                "group": "MSMA",
                "investigators": [
                {
                    "name": "Mathew Summers",
                    "abbreviation": None,
                    "registry": None,
                    "registry_identifier": None
                },
                {
                    "name": "Jayaram Chandrashekar",
                    "abbreviation": None,
                    "registry": None,
                    "registry_identifier": None
                }
                ],
                "project_name": "Thalamus in the middle",
                "restrictions": None,
                "modality": [
                {
                    "name": "Selective plane illumination microscopy",
                    "abbreviation": "SPIM"
                }
                ],
                "related_data": [],
                "data_summary": None
            },
        }
    )

    sample_instrument = json.dumps(
        {
            "instrument": {
                "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/imaging/instrument.py",
                "schema_version": "0.5.4",
                "instrument_id": "SmartSPIM1-2",
                "instrument_type": "SmartSPIM",
                "location": "615 Westlake",
                "manufacturer": "LifeCanvas",
                "temperature_control": None,
                "humidity_control": False,
                "optical_tables": [
                {
                    "name": None,
                    "serial_number": "Unknown",
                    "manufacturer": "MKS Newport",
                    "model": "VIS3648-PG4-325A",
                    "notes": None,
                    "length": 36,
                    "width": 48,
                    "table_size_unit": "inch",
                    "vibration_control": True
                }
                ],
                "objectives": [
                {
                    "name": None,
                    "serial_number": "Unknown",
                    "manufacturer": "Thorlabs",
                    "model": "TL4X-SAP",
                    "notes": "Thorlabs TL4X-SAP with LifeCanvas dipping cap and correction optics",
                    "numerical_aperture": 0.2,
                    "magnification": 3.6,
                    "immersion": "multi"
                }
                ],
                "detectors": [
                {
                    "name": None,
                    "serial_number": "220302-SYS-060443",
                    "manufacturer": "Hamamatsu",
                    "model": "C14440-20UP",
                    "notes": None,
                    "type": "Camera",
                    "data_interface": "USB",
                    "cooling": "water"
                }
                ],
                "light_sources": [
                {
                    "name": None,
                    "serial_number": "VL08223M03",
                    "manufacturer": "Vortran",
                    "model": "Stradus",
                    "notes": "All lasers controlled via Vortran VersaLase System",
                    "type": "laser",
                    "coupling": "Single-mode fiber",
                    "wavelength": 445,
                    "wavelength_unit": "nanometer",
                    "max_power": 150,
                    "power_unit": "milliwatt"
                }
                ],
                "fluorescence_filters": [
                {
                    "name": None,
                    "serial_number": "Unknown-0",
                    "manufacturer": "Semrock",
                    "model": "FF01-469/35-25",
                    "notes": None,
                    "filter_type": "Band pass",
                    "diameter": 25,
                    "diameter_unit": "millimeter",
                    "thickness": 2,
                    "thickness_unit": "millimeter",
                    "filter_wheel_index": 0,
                    "cut_off_frequency": None,
                    "cut_off_frequency_unit": "Hertz",
                    "cut_on_frequency": None,
                    "cut_on_frequency_unit": "Hertz",
                    "description": None
                }
                ],
                "motorized_stages": [
                {
                    "name": None,
                    "serial_number": "Unknown-0",
                    "manufacturer": "Applied Scientific Instrumentation",
                    "model": "LS-100",
                    "notes": "Focus stage",
                    "travel": 100,
                    "travel_unit": "millimeter"
                }
                ],
                "scanning_stages": [
                {
                    "name": None,
                    "serial_number": "Unknown-1",
                    "manufacturer": "Applied Scientific Instrumentation",
                    "model": "LS-50",
                    "notes": "Sample stage X",
                    "travel": 50,
                    "travel_unit": "millimeter",
                    "stage_axis_direction": "Illumination axis",
                    "stage_axis_name": "X"
                },

                ],
                "daqs": None,
                "additional_devices": [
                {
                    "name": None,
                    "serial_number": "10436130",
                    "manufacturer": "Julabo",
                    "model": "200F",
                    "notes": None,
                    "type": "Other"
                }
                ],
                "calibration_date": None,
                "calibration_data": None,
                "com_ports": [
                {
                    "hardware_name": "Laser Launch",
                    "com_port": "COM3"
                }
                ],
                "notes": None
            },
        }
    )

    sample_procedures =  json.dumps(
        {
            "procedures": {
                "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/core/procedures.py",
                "schema_version": "0.11.2",
                "subject_id": "662616",
                "subject_procedures": [
                {
                    "procedure_type": "Surgery",
                    "start_date": "2023-02-03",
                    "experimenter_full_name": "30509",
                    "iacuc_protocol": None,
                    "animal_weight_prior": None,
                    "animal_weight_post": None,
                    "weight_unit": "gram",
                    "anaesthesia": None,
                    "workstation_id": None,
                    "procedures": [
                    {
                        "procedure_type": "Perfusion",
                        "protocol_id": "dx.doi.org/10.17504/protocols.io.bg5vjy66",
                        "output_specimen_ids": [
                        "662616"
                        ]
                    }
                    ],
                    "notes": None
                },
                {
                    "procedure_type": "Surgery",
                    "start_date": "2023-01-05",
                    "experimenter_full_name": "NSB-5756",
                    "iacuc_protocol": "2109",
                    "animal_weight_prior": "16.6",
                    "animal_weight_post": "16.7",
                    "weight_unit": "gram",
                    "anaesthesia": {
                    "type": "isoflurane",
                    "duration": "120.0",
                    "duration_unit": "minute",
                    "level": "1.5"
                    },
                    "workstation_id": "SWS 1",
                    "procedures": [
                    {
                        "injection_materials": [
                        {
                            "material_type": "Virus",
                            "name": "SL1-hSyn-Cre",
                            "tars_identifiers": {
                            "virus_tars_id": None,
                            "plasmid_tars_alias": None,
                            "prep_lot_number": "221118-11",
                            "prep_date": None,
                            "prep_type": None,
                            "prep_protocol": None
                            },
                            "addgene_id": None,
                            "titer": {
                            "$numberLong": "37500000000000"
                            },
                            "titer_unit": "gc/mL"
                        }
                        ],
                        "recovery_time": "10.0",
                        "recovery_time_unit": "minute",
                        "injection_duration": None,
                        "injection_duration_unit": "minute",
                        "instrument_id": "NJ#2",
                        "protocol_id": "dx.doi.org/10.17504/protocols.io.bgpujvnw",
                        "injection_coordinate_ml": "0.35",
                        "injection_coordinate_ap": "2.2",
                        "injection_coordinate_depth": [
                        "2.1"
                        ],
                        "injection_coordinate_unit": "millimeter",
                        "injection_coordinate_reference": "Bregma",
                        "bregma_to_lambda_distance": "4.362",
                        "bregma_to_lambda_unit": "millimeter",
                        "injection_angle": "0",
                        "injection_angle_unit": "degrees",
                        "targeted_structure": "mPFC",
                        "injection_hemisphere": "Right",
                        "procedure_type": "Nanoject injection",
                        "injection_volume": [
                        "200"
                        ],
                        "injection_volume_unit": "nanoliter"
                    },
                    {
                        "injection_materials": [
                        {
                            "material_type": "Virus",
                            "name": "AAV-Syn-DIO-TVA66T-dTomato-CVS N2cG",
                            "tars_identifiers": {
                            "virus_tars_id": None,
                            "plasmid_tars_alias": None,
                            "prep_lot_number": "220916-4",
                            "prep_date": None,
                            "prep_type": None,
                            "prep_protocol": None
                            },
                            "addgene_id": None,
                            "titer": {
                            "$numberLong": "18000000000000"
                            },
                            "titer_unit": "gc/mL"
                        }
                        ],
                        "recovery_time": "10.0",
                        "recovery_time_unit": "minute",
                        "injection_duration": None,
                        "injection_duration_unit": "minute",
                        "instrument_id": "NJ#2",
                        "protocol_id": "dx.doi.org/10.17504/protocols.io.bgpujvnw",
                        "injection_coordinate_ml": "2.9",
                        "injection_coordinate_ap": "-0.6",
                        "injection_coordinate_depth": [
                        "3.6"
                        ],
                        "injection_coordinate_unit": "millimeter",
                        "injection_coordinate_reference": "Bregma",
                        "bregma_to_lambda_distance": "4.362",
                        "bregma_to_lambda_unit": "millimeter",
                        "injection_angle": "30",
                        "injection_angle_unit": "degrees",
                        "targeted_structure": "VM",
                        "injection_hemisphere": "Right",
                        "procedure_type": "Nanoject injection",
                        "injection_volume": [
                        "200"
                        ],
                        "injection_volume_unit": "nanoliter"
                    }
                    ],
                    "notes": None
                }
                ],
                "specimen_procedures": [
                {
                    "procedure_type": "Fixation",
                    "procedure_name": "SHIELD OFF",
                    "specimen_id": "662616",
                    "start_date": "2023-02-10",
                    "end_date": "2023-02-12",
                    "experimenter_full_name": "DT",
                    "protocol_id": "none",
                    "reagents": [
                    {
                        "name": "SHIELD Epoxy",
                        "source": "LiveCanvas Technologies",
                        "rrid": None,
                        "lot_number": "unknown",
                        "expiration_date":None
                    }
                    ],
                    "hcr_series": None,
                    "immunolabeling": None,
                    "notes": "None"
                },
                ],
                "notes": None
            },
        }
    )
    
    sample_subject = json.dumps(
        {
            "subject": {
                "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/subject.py",
                "schema_version": "0.4.2",
                "species": {
                "name": "Mus musculus",
                "abbreviation": None,
                "registry": {
                    "name": "National Center for Biotechnology Information",
                    "abbreviation": "NCBI"
                },
                "registry_identifier": "10090"
                },
                "subject_id": "662616",
                "sex": "Female",
                "date_of_birth": "2022-11-29",
                "genotype": "wt/wt",
                "mgi_allele_ids": None,
                "background_strain": None,
                "source": None,
                "rrid": None,
                "restrictions": None,
                "breeding_group": None,
                "maternal_id": None,
                "maternal_genotype": None,
                "paternal_id": None,
                "paternal_genotype": None,
                "wellness_reports": None,
                "housing": None,
                "notes": None
            }
        }
    )

    sample_processing = json.dumps(
        {
        "processing": {
            "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/core/processing.py",
            "schema_version": "1.0.0",
            "processing_pipeline": {
                "data_processes": [],
                "processor_full_name": "AIND Scientific Computing",
                "pipeline_version": None,
                "pipeline_url": None,
                "note": None
            },
            "analyses": [],
            "notes": None
            }
        }
    )
    sample_rig = json.dumps(
        {
        "rig": {
            "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/core/rig.py",
            "schema_version": "0.3.8",
            "rig_id": "447-2-B_20240827",
            "modification_date": "2024-08-27",
            "mouse_platform": {
                "device_type": "Tube",
                "name": "mouse_tube_foraging",
                "serial_number": None,
                "manufacturer": {
                "name": "Custom",
                "abbreviation": None,
                "registry": None,
                "registry_identifier": None
                },
                "model": None,
                "path_to_cad": None,
                "port_index": None,
                "additional_settings": {},
                "notes": None,
                "surface_material": None,
                "date_surface_replaced": None,
                "diameter": "3.0",
                "diameter_unit": "centimeter"
            },
            "stimulus_devices": [
                {
                "device_type": "Reward delivery",
                "stage_type": {
                    "device_type": "Motorized stage",
                    "name": "NewScaleMotor for LickSpouts",
                    "serial_number": "46801",
                    "manufacturer": {
                    "name": "New Scale Technologies",
                    "abbreviation": None,
                    "registry": None,
                    "registry_identifier": None
                    },
                    "model": "XYZ Stage with M30LS-3.4-15 linear stages",
                    "path_to_cad": None,
                    "port_index": None,
                    "additional_settings": {},
                    "notes": None,
                    "travel": "15.0",
                    "travel_unit": "millimeter",
                    "firmware": "https://github.com/AllenNeuralDynamics/python-newscale, branch: axes-on-target, commit #7c17497"
                },
                "reward_spouts": [
                    {
                    "device_type": "Reward spout",
                    "name": "Left lick spout",
                    "serial_number": None,
                    "manufacturer": None,
                    "model": None,
                    "path_to_cad": None,
                    "port_index": None,
                    "additional_settings": {},
                    "notes": None,
                    "side": "Left",
                    "spout_diameter": "1.2",
                    "spout_diameter_unit": "millimeter",
                    "spout_position": None,
                    "solenoid_valve": {
                        "device_type": "Solenoid",
                        "name": "Solenoid Left",
                        "serial_number": None,
                        "manufacturer": {
                        "name": "The Lee Company",
                        "abbreviation": None,
                        "registry": None,
                        "registry_identifier": None
                        },
                        "model": "LHDA1233415H",
                        "path_to_cad": None,
                        "port_index": None,
                        "additional_settings": {},
                        "notes": None
                    },
                    "lick_sensor": {
                        "device_type": "Lick Sensor",
                        "name": "Lick Sensor Left",
                        "serial_number": None,
                        "manufacturer": {
                        "name": "Janelia Research Campus",
                        "abbreviation": "Janelia",
                        "registry": {
                            "name": "Research Organization Registry",
                            "abbreviation": "ROR"
                        },
                        "registry_identifier": "013sk6x84"
                        },
                        "model": None,
                        "path_to_cad": None,
                        "port_index": None,
                        "additional_settings": {},
                        "notes": None
                    },
                    "lick_sensor_type": "Capacitive"
                    }
                ]
                },
                {
                "device_type": "Speaker",
                "name": "Stimulus Speaker",
                "serial_number": None,
                "manufacturer": {
                    "name": "Tymphany",
                    "abbreviation": None,
                    "registry": None,
                    "registry_identifier": None
                },
                "model": "XT25SC90-04",
                "path_to_cad": None,
                "port_index": None,
                "additional_settings": {},
                "notes": None,
                "position": None
                }
            ],
            "cameras": [
                {
                "name": "BehaviorVideography_FaceSide",
                "camera_target": "Face side right",
                "camera": {
                    "device_type": "Detector",
                    "name": "Side face camera",
                    "serial_number": None,
                    "manufacturer": {
                    "name": "Ailipu Technology Co",
                    "abbreviation": None,
                    "registry": None,
                    "registry_identifier": None
                    },
                    "model": "ELP-USBFHD05MT-KL170IR",
                    "path_to_cad": None,
                    "port_index": None,
                    "additional_settings": {},
                    "notes": "The light intensity sensor was removed; IR illumination is constantly on",
                    "detector_type": "Camera",
                    "data_interface": "USB",
                    "cooling": "Air",
                    "computer_name": "W10DT714084",
                    "max_frame_rate": "120",
                    "frame_rate_unit": "hertz",
                    "immersion": None,
                    "chroma": "Color",
                    "sensor_width": 640,
                    "sensor_height": 480,
                    "size_unit": "pixel",
                    "sensor_format": None,
                    "sensor_format_unit": None,
                    "bit_depth": None,
                    "bin_mode": "Additive",
                    "bin_width": None,
                    "bin_height": None,
                    "bin_unit": "pixel",
                    "gain": None,
                    "crop_width": None,
                    "crop_height": None,
                    "crop_unit": "pixel",
                    "recording_software": {
                    "name": "Bonsai",
                    "version": "2.8.0",
                    "url": None,
                    "parameters": {}
                    },
                    "driver": None,
                    "driver_version": None
                },
                "lens": {
                    "device_type": "Lens",
                    "name": "Xenocam 1",
                    "serial_number": None,
                    "manufacturer": {
                    "name": "Other",
                    "abbreviation": None,
                    "registry": None,
                    "registry_identifier": None
                    },
                    "model": "XC0922LENS",
                    "path_to_cad": None,
                    "port_index": None,
                    "additional_settings": {},
                    "notes": "Manufacturer is Xenocam",
                    "focal_length": "9",
                    "focal_length_unit": "millimeter",
                    "size": None,
                    "lens_size_unit": "inch",
                    "optimized_wavelength_range": None,
                    "wavelength_unit": "nanometer",
                    "max_aperture": "f/1.4"
                },
                "filter": None,
                "position": None
                }
            ],
            "enclosure": {
                "device_type": "Enclosure",
                "name": "Behavior enclosure",
                "serial_number": None,
                "manufacturer": {
                "name": "Allen Institute for Neural Dynamics",
                "abbreviation": "AIND",
                "registry": {
                    "name": "Research Organization Registry",
                    "abbreviation": "ROR"
                },
                "registry_identifier": "04szwah67"
                },
                "model": None,
                "path_to_cad": None,
                "port_index": None,
                "additional_settings": {},
                "notes": None,
                "size": {
                "width": 54,
                "length": 54,
                "height": 54,
                "unit": "centimeter"
                },
                "internal_material": "",
                "external_material": "",
                "grounded": False,
                "laser_interlock": False,
                "air_filtration": False
            },
            "ephys_assemblies": [],
            "fiber_assemblies": [],
            "stick_microscopes": [],
            "laser_assemblies": [],
            "patch_cords": [],
            "light_sources": [
                {
                "device_type": "Light emitting diode",
                "name": "IR LED",
                "serial_number": None,
                "manufacturer": {
                    "name": "Thorlabs",
                    "abbreviation": None,
                    "registry": {
                    "name": "Research Organization Registry",
                    "abbreviation": "ROR"
                    },
                    "registry_identifier": "04gsnvb07"
                },
                "model": "M810L5",
                "path_to_cad": None,
                "port_index": None,
                "additional_settings": {},
                "notes": None,
                "wavelength": 810,
                "wavelength_unit": "nanometer"
                }
            ],
            "detectors": [],
            "objectives": [],
            "filters": [],
            "lenses": [],
            "digital_micromirror_devices": [],
            "polygonal_scanners": [],
            "pockels_cells": [],
            "additional_devices": [],
            "daqs": [
                {
                "device_type": "Harp device",
                "name": "Harp Behavior",
                "serial_number": None,
                "manufacturer": {
                    "name": "Champalimaud Foundation",
                    "abbreviation": None,
                    "registry": {
                    "name": "Research Organization Registry",
                    "abbreviation": "ROR"
                    },
                    "registry_identifier": "03g001n57"
                },
                "model": None,
                "path_to_cad": None,
                "port_index": None,
                "additional_settings": {},
                "notes": "Left lick spout and Right lick spout, as well as reward delivery solenoids are connected via ethernet cables",
                "data_interface": "Ethernet",
                "computer_name": "W10DT714084",
                "channels": [],
                "firmware_version": None,
                "hardware_version": None,
                "harp_device_type": {
                    "name": "Behavior",
                    "whoami": 1216
                },
                "core_version": "1.11",
                "tag_version": None,
                "is_clock_generator": False
                }
            ],
            "calibrations": [
                {
                "calibration_date": "2024-08-27T00:00:00-07:00",
                "device_name": "Lick spout Left",
                "description": "Water calibration for Lick spout Left. The input is the valve open time in seconds and the output is the volume of water delivered in microliters.",
                "input": {
                    "valve open time (s):": [
                    0.02,
                    0.025,
                    0.03
                    ]
                },
                "output": {
                    "water volume (ul):": [
                    1.35,
                    2,
                    2.5,
                    ]
                },
                "notes": None
                }
            ],
            "ccf_coordinate_transform": None,
            "origin": None,
            "rig_axes": None,
            "modalities": [
                {
                "name": "Behavior videos",
                "abbreviation": "behavior-videos"
                },
                {
                "name": "Behavior",
                "abbreviation": "behavior"
                }
            ],
            "notes": None
            }
        }
    )
    sample_session = json.dumps(
        {
            "session": {
                "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/core/session.py",
                "schema_version": "0.2.6",
                "protocol_id": [
                    ""
                ],
                "experimenter_full_name": [
                    "Bowen Tan"
                ],
                "session_start_time": "2024-09-03T15:49:53.900668-07:00",
                "session_end_time": "2024-09-03T17:04:59.585169-07:00",
                "session_type": "Uncoupled Baiting",
                "iacuc_protocol": "2109",
                "rig_id": "447-2-B_20240827",
                "calibrations": [],
                "maintenance": [],
                "subject_id": "730945",
                "animal_weight_prior": None,
                "animal_weight_post": "23.6",
                "weight_unit": "gram",
                "anaesthesia": None,
                "data_streams": [
                    {
                    "stream_start_time": "2024-09-03T15:49:53.900668-07:00",
                    "stream_end_time": "2024-09-03T17:04:59.585169-07:00",
                    "daq_names": [
                        "Harp Behavior",
                        "Harp Sound",
                        "Harp clock synchronization board",
                        "Harp sound amplifier",
                        "Lick Sensor Left",
                        "Lick Sensor Right"
                    ],
                    "camera_names": [],
                    "light_sources": [],
                    "ephys_modules": [],
                    "stick_microscopes": [],
                    "manipulator_modules": [],
                    "detectors": [],
                    "fiber_connections": [],
                    "fiber_modules": [],
                    "ophys_fovs": [],
                    "slap_fovs": None,
                    "stack_parameters": None,
                    "mri_scans": [],
                    "stream_modalities": [
                        {
                        "name": "Behavior",
                        "abbreviation": "behavior"
                        }
                    ],
                    "software": [
                        {
                        "name": "dynamic-foraging-task",
                        "version": "behavior branch:main   commit ID:04bcaa08294ead9ae3b9a08ff040c09f0999c782    version:1.4.4; metadata branch: main   commit ID:04bcaa08294ead9ae3b9a08ff040c09f0999c782   version:1.4.4",
                        "url": "https://github.com/AllenNeuralDynamics/dynamic-foraging-task.git",
                        "parameters": {}
                        }
                    ],
                    "notes": None
                    }
                ],
                "stimulus_epochs": [
                    {
                    "stimulus_start_time": "2024-09-03T15:49:53.900668-07:00",
                    "stimulus_end_time": "2024-09-03T17:04:59.585169-07:00",
                    "stimulus_name": "auditory go cue",
                    "session_number": None,
                    "software": [
                        {
                        "name": "dynamic-foraging-task",
                        "version": "behavior branch:main   commit ID:04bcaa08294ead9ae3b9a08ff040c09f0999c782    version:1.4.4; metadata branch: main   commit ID:04bcaa08294ead9ae3b9a08ff040c09f0999c782   version:1.4.4",
                        "url": "https://github.com/AllenNeuralDynamics/dynamic-foraging-task.git",
                        "parameters": {}
                        }
                    ],
                    "script": None,
                    "stimulus_modalities": [
                        "Auditory"
                    ],
                    "stimulus_parameters": [
                        {
                        "stimulus_type": "Auditory Stimulation",
                        "sitmulus_name": "auditory go cue",
                        "sample_frequency": "96000",
                        "amplitude_modulation_frequency": 7500,
                        "frequency_unit": "hertz",
                        "bandpass_low_frequency": None,
                        "bandpass_high_frequency": None,
                        "bandpass_filter_type": None,
                        "bandpass_order": None,
                        "notes": None
                        }
                    ],
                    "stimulus_device_names": [],
                    "speaker_config": {
                        "name": "Stimulus Speaker",
                        "volume": "76",
                        "volume_unit": "decibels"
                    },
                    "light_source_config": None,
                    "output_parameters": {
                        "meta": {
                        "box": "447-2-B",
                        "session_end_time": "2024-09-03 17:04:59.585169",
                        "session_run_time_in_min": 75
                        },
                        "water": {
                        "water_in_session_foraging": 0.372,
                        "water_in_session_manual": 0.09599999999999997,
                        "water_in_session_total": 0.46799999999999997,
                        "water_after_session": 0.532,
                        "water_day_total": 1
                        },
                        "weight": {
                        "base_weight": 23.18,
                        "target_weight": 19.703,
                        "target_weight_ratio": 0.85,
                        "weight_after": 23.6
                        },
                        "performance": {
                        "foraging_efficiency": 0.5931917753463685,
                        "foraging_efficiency_with_actual_random_seed": 0.6138613861386139
                        },
                        "task_parameters": {
                        "SessionlistSpin": "1",
                        "qt_spinbox_lineedit": "3.00",
                        "Load": False,
                        "NewSession": False,
                        "Clear": False,
                        "Start": False,
                        "Save": False,
                        "Sessionlist": "",
                        "HideLegend": False,
                        "ID": "730945",
                        "Experimenter": "Bowen Tan",
                        "AutoTrain": False,
                        "pushButton_streamlit": False,
                        "StartFIP": False,
                        "StartExcitation": False,
                        "StartBleaching": False,
                        "FIPMode": "Normal",
                        "baselinetime": "10",
                        "PhotometryB": "off",
                        "OptogeneticsB": "off",
                        "StartEphysRecording": False,
                        "OpenEphysRecordingType": "Behavior",
                        "MoveYN": False,
                        "MoveZN": False,
                        "StageStop": False,
                        "MoveYP": False,
                        "MoveZP": False,
                        "MoveXN": False,
                        "MoveXP": False,
                        "PositionZ": "6358.5",
                        "PositionY": "14387.5",
                        "PositionX": "6400.0",
                        "Step": "200",
                        "SetReference": False,
                        "GetPositions": False,
                        "StepSize": "5",
                        "WindowSize": "100",
                        "RunLength": "10",
                        "MartchingType": "log ratio",
                        "TargetRatio": "0.85",
                        "TotalWater": "1.0",
                        "SuggestedWater": "0.532",
                        "BaseWeight": "23.18",
                        "TargetWeight": "19.703",
                        "WeightAfter": "23.6",
                        "ShowNotes": "",
                        "ITIMin": "1.0",
                        "DelayMin": "1.0",
                        "InitiallyInactiveN": "2",
                        "DelayBeta": "0.0",
                        "DelayMax": "1.0",
                        "BlockMinReward": "0",
                        "AutoReward": False,
                        "ITIIncrease": "0",
                        "AutoWaterType": "Natural",
                        "Task": "Uncoupled Baiting",
                        "BlockMax": "35",
                        "RewardDelay": "0.0",
                        "SwitchThr": "0.5",
                        "ITIMax": "30.0",
                        "ITIBeta": "3.0",
                        "ResponseTime": "1.0",
                        "PointsInARow": "5",
                        "AdvancedBlockAuto": "now",
                        "Ignored": "10",
                        "BlockBeta": "10",
                        "BlockMin": "20",
                        "StopIgnores": "25",
                        "RewardPairsN": "1",
                        "MaxTime": "75",
                        "RewardConsumeTime": "3.0",
                        "NextBlock": False,
                        "IncludeAutoReward": "no",
                        "Multiplier": "0.5",
                        "RewardFamily": "1",
                        "RightValue_volume": "2.00",
                        "UncoupledReward": "0.1, 0.4, 0.7",
                        "RightValue": "0.023",
                        "BaseRewardSum": "0.8",
                        "LeftValue": "0.025",
                        "MaxTrial": "1000",
                        "Unrewarded": "10",
                        "LeftValue_volume": "2.00",
                        "warm_windowsize": "20",
                        "warm_max_choice_ratio_bias": "0.1",
                        "warmup": "off",
                        "warm_min_finish_ratio": "0.8",
                        "warm_min_trial": "50",
                        "Randomness": "Exponential",
                        "AddOneTrialForNoresponse": "Yes",
                        "GiveRight": False,
                        "GiveWaterL": "0.034",
                        "GiveWaterR": "0.035",
                        "GiveWaterL_volume": "3.00",
                        "GiveWaterR_volume": "3.00",
                        "GiveLeft": False,
                        "AlignToGoCue": "yes",
                        "MoveXP_2": False,
                        "MoveXN_2": False,
                        "LaserCalibration_dialog": {
                            "Frequency_1": "40",
                            "Protocol_1": "Sine",
                            "Location_1": "Both",
                            "Duration_1": "10",
                            "RD_1": "1",
                            "LaserColor_1": "Blue",
                            "PulseDur_1": "0.002",
                            "KeepOpen": False,
                            "SampleFrequency": "5000",
                            "CopyFromOpto": False,
                            "LaserPowerMeasured": "",
                            "Save": False,
                            "voltage": "0.1",
                            "Capture": False,
                            "Flush_DO0": False,
                            "Flush_DO1": False,
                            "Flush_DO2": False,
                            "Flush_DO3": False,
                            "Flush_Port2": False,
                            "showrecentlaser": "",
                            "qt_spinbox_lineedit": "",
                            "showspecificcalilaser": "NA",
                            "CopyToSession": False,
                            "CopyCondition": "Condition_1",
                            "CopyLaser": "Laser_1",
                            "Open": False
                        },
                        "Opto_dialog": {
                            "MinOptoInterval": "0",
                            "SessionWideControl": "off",
                            "FractionOfSession": "0.5",
                            "SessionStartWith": "on",
                            "SessionAlternating": "on",
                            "SampleFrequency": "5000",
                            "LatestCalibrationDate": "NA",
                            "Laser_calibration": "Blue",
                            "laser_1_target": "",
                            "laser_2_target": "",
                            "laser_2_calibration_voltage": "",
                            "laser_1_calibration_power": "",
                            "laser_1_calibration_voltage": "",
                            "laser_2_calibration_power": "",
                            "OffsetStart_2": "0",
                            "Probability_2": "0.25",
                            "OffsetEnd_2": "0",
                            "Duration_2": "5",
                            "LaserEnd_2": "Trial start",
                            "RD_2": "1",
                            "LaserColor_2": "NA",
                            "Location_2": "Both",
                            "Frequency_2": "40",
                            "Laser2_power_2": "0 mw",
                            "Laser1_power_2": "0 mw",
                            "LaserStart_2": "Trial start",
                            "Protocol_2": "Sine",
                            "Condition_2": "NA",
                            "Laser2_power_3": "0 mw",
                            "Location_3": "Both",
                            "LaserStart_3": "Trial start",
                            "LaserEnd_3": "Trial start",
                            "OffsetEnd_3": "0",
                            "Condition_3": "NA",
                            "OffsetStart_3": "0",
                            "LaserColor_3": "NA",
                            "Protocol_3": "Sine",
                            "Laser1_power_3": "0 mw",
                            "Duration_3": "5",
                            "Probability_3": "0.25",
                            "Frequency_3": "40",
                            "RD_3": "1",
                            "LaserStart_4": "Trial start",
                            "Laser1_power_4": "0 mw",
                            "Duration_4": "5",
                            "LaserColor_4": "NA",
                            "OffsetStart_4": "0",
                            "Laser2_power_4": "0 mw",
                            "LaserEnd_4": "Trial start",
                            "OffsetEnd_4": "0",
                            "Location_4": "Both",
                            "Probability_4": "0.25",
                            "Condition_4": "NA",
                            "Frequency_4": "40",
                            "Protocol_4": "Sine",
                            "RD_4": "1",
                            "LaserStart_5": "Trial start",
                            "LaserColor_5": "NA",
                            "Probability_1": "0.25",
                            "Laser1_power_1": "0 mw",
                            "LaserColor_1": "NA",
                            "Location_1": "Both",
                            "Laser2_power_1": "0 mw",
                            "RD_1": "1",
                            "Frequency_1": "40",
                            "OffsetEnd_1": "0",
                            "LaserEnd_1": "Trial start",
                            "Duration_1": "5",
                            "Condition_1": "NA",
                            "LaserStart_1": "Trial start",
                            "OffsetStart_1": "0",
                            "Protocol_1": "Sine",
                            "OffsetEnd_5": "0",
                            "PulseDur_2": "0.002",
                            "Laser2_power_5": "0 mw",
                            "LaserEnd_5": "Trial start",
                            "Probability_5": "0.25",
                            "Frequency_5": "40",
                            "Duration_5": "5",
                            "Protocol_5": "Sine",
                            "ConditionP_5": "1",
                            "PulseDur_4": "0.002",
                            "Condition_5": "NA",
                            "RD_5": "1",
                            "PulseDur_1": "0.002",
                            "PulseDur_3": "0.002",
                            "ConditionP_4": "1",
                            "ConditionP_2": "1",
                            "PulseDur_5": "0.002",
                            "ConditionP_3": "1",
                            "OffsetStart_5": "0",
                            "Laser1_power_5": "0 mw",
                            "Location_5": "Both",
                            "ConditionP_1": "1",
                            "LaserColor_6": "NA",
                            "LaserStart_6": "Trial start",
                            "Location_6": "Both",
                            "OffsetStart_6": "0",
                            "Laser1_power_6": "0 mw",
                            "LaserEnd_6": "Trial start",
                            "Laser2_power_6": "0 mw",
                            "OffsetEnd_6": "0",
                            "Probability_6": "0.25",
                            "Protocol_6": "Sine",
                            "Duration_6": "5",
                            "Frequency_6": "40",
                            "Condition_6": "NA",
                            "RD_6": "1",
                            "ConditionP_6": "1",
                            "PulseDur_6": "0.002"
                        },
                        "Camera_dialog": {
                            "StartRecording": False,
                            "AutoControl": "No",
                            "FrameRate": "500",
                            "qt_spinbox_lineedit": "500",
                            "OpenSaveFolder": False,
                            "StartPreview": False,
                            "camera_start_time": "",
                            "camera_stop_time": ""
                        },
                        "Metadata_dialog": {
                            "RotationAngle": "",
                            "EphysProbes": "",
                            "ModuleAngle": "",
                            "ArcAngle": "",
                            "ManipulatorX": "",
                            "ManipulatorZ": "",
                            "ManipulatorY": "",
                            "ProbeTarget": "",
                            "ExperimentDescription": "Behavior training\n",
                            "SaveMeta": False,
                            "IACUCProtocol": "2109",
                            "ProtocolID": "",
                            "RigMetadataFile": "rig_447-2-B_2024-08-27_10_53_22.json",
                            "SelectRigMetadata": False,
                            "ClearMetadata": False,
                            "StickMicroscopes": "",
                            "Stick_ModuleAngle": "",
                            "Stick_ArcAngle": "",
                            "Stick_RotationAngle": "",
                            "DataSummary": "",
                            "FundingSource": "",
                            "Investigators": "",
                            "ProjectName": "",
                            "GrantNumber": "",
                            "Fundee": "",
                            "LoadMeta": False,
                            "GoCueDecibel": "76",
                            "LickSpoutReferenceZ": "",
                            "LickSpoutReferenceY": "",
                            "LickSpoutReferenceX": "",
                            "LickSpoutReferenceArea": "",
                            "LickSpoutDistance": "5000"
                        },
                        "Other_CurrentTime": "2024-09-03 17:04:59.585169",
                        "Other_RunningTime": 75,
                        "Other_SessionStartTime": "2024-09-03 15:49:53.900668",
                        "Other_current_box": "447-2-B",
                        "Other_go_cue_decibel": "76",
                        "Other_lick_spout_distance": "5000",
                        "info_performance_essential_1": "Current trial: 493\nResponded trial: 434/493 (0.88)\nReward Trial: 186/493 (0.38)\nEarned Reward: 0.372 mL\nWater in session: 0.468 mL",
                        "info_performance_essential_2": "Foraging eff: 0.59\nForaging eff (r.s.): 0.61\n\nBias: -1.26 (left)",
                        "info_performance_others": "Left choice rewarded: 125/352 (0.36)\nRight choice rewarded: 61/82 (0.74)\n\nEarly licking (EL)\n  Frac of EL trial start_goCue: 243/492 (0.49)\n  Frac of EL trial start_delay: 212/492 (0.43)\n  Frac of EL trial delay_goCue: 90/492 (0.18)\n  Left/Right early licks start_goCue: 778/152 (5.12)\n\nDouble dipping (DD)\n  Frac of DD trial start_goCue: 27/492 (0.05)\n  Frac of DD trial start_delay: 15/492 (0.03)\n  Frac of DD trial delay_goCue: 13/492 (0.03)\n  Frac of DD trial goCue_goCue1: 16/492 (0.03)\n  DD per finish trial start_goCue: 0.1\n  DD per finish trial goCue_goCue1: 0.04\n\n  Frac of DD trial goCue_nextStart: 31/491 (0.06)\n  DD per finish trial goCue_nextStart: 0.08\n",
                        "info_task": "Session started: 15:49\nCurrent time: 17:04\nRun time: 75 mins\n\nCurrent left block: 11/24\nCurrent right block: 30/32",
                        "Ot_log_folder": "C:\\behavior_data\\447-2-B\\730945\\behavior_730945_2024-09-03_15-49-53\\behavior\\raw.harp",
                        "box": "447-2-B",
                        "settings": {
                            "default_saveFolder": "C:\\behavior_data\\",
                            "current_box": "447-2",
                            "Teensy_COM_box1": "",
                            "Teensy_COM_box2": "",
                            "Teensy_COM_box3": "",
                            "Teensy_COM_box4": "",
                            "bonsai_path": "C:\\Users\\svc_aind_behavior\\Documents\\Github\\dynamic-foraging-task\\bonsai\\Bonsai.exe",
                            "bonsaiworkflow_path": "C:\\Users\\svc_aind_behavior\\Documents\\Github\\dynamic-foraging-task\\src\\workflows\\foraging.bonsai",
                            "temporary_video_folder": "C:\\Users\\svc_aind_behavior\\Documents\\temporaryvideo\\",
                            "show_log_info_in_console": False,
                            "newscale_serial_num_box1": "46103",
                            "newscale_serial_num_box2": "46801",
                            "newscale_serial_num_box3": "",
                            "newscale_serial_num_box4": "",
                            "default_ui": "ForagingGUI.ui",
                            "create_rig_metadata": True,
                            "go_cue_decibel_box1": 75,
                            "go_cue_decibel_box2": 76,
                            "go_cue_decibel_box3": 75,
                            "go_cue_decibel_box4": 75,
                            "FIP_workflow_path": "",
                            "FIP_settings": "C:\\Users\\svc_aind_behavior\\Documents\\FIPSettings",
                            "bonsai_config_path": "C:\\Users\\svc_aind_behavior\\Documents\\GitHub\\dynamic-foraging-task\\bonsai\\Bonsai.config",
                            "open_ephys_machine_ip_address": "",
                            "metadata_dialog_folder": "C:\\Users\\svc_aind_behavior\\Documents\\ForagingSettings\\metadata_dialog\\",
                            "rig_metadata_folder": "C:\\Users\\svc_aind_behavior\\Documents\\ForagingSettings\\rig_metadata\\",
                            "project_info_file": "C:\\Users\\svc_aind_behavior\\Documents\\ForagingSettings\\Project Name and Funding Source v2.csv",
                            "schedule_path": "Z:\\dynamic_foraging\\DynamicForagingSchedule.csv",
                            "lick_spout_distance_box1": 5000,
                            "lick_spout_distance_box2": 5000,
                            "lick_spout_distance_box3": 5000,
                            "lick_spout_distance_box4": 5000,
                            "name_mapper_file": "C:\\Users\\svc_aind_behavior\\Documents\\ForagingSettings\\name_mapper.json",
                            "save_each_trial": True,
                            "AutomaticUpload": True,
                            "manifest_flag_dir": "C:\\Users\\svc_aind_behavior\\Documents\\aind_watchdog_service\\manifest",
                            "auto_engage": True,
                            "clear_figure_after_save": True,
                            "default_openFolder": "C:\\behavior_data\\"
                        },
                        "settings_box": {
                            "Behavior": "COM7",
                            "Soundcard": "COM5",
                            "BonsaiOsc1": "4012",
                            "BonsaiOsc2": "4013",
                            "BonsaiOsc3": "4014",
                            "BonsaiOsc4": "4015",
                            "HighSpeedCamera": "0",
                            "AINDLickDetector": "0",
                            "AttenuationLeft": "50",
                            "AttenuationRight": "50",
                            "current_box": "447-2-B"
                        },
                        "commit_ID": "04bcaa08294ead9ae3b9a08ff040c09f0999c782",
                        "repo_url": "https://github.com/AllenNeuralDynamics/dynamic-foraging-task.git",
                        "current_branch": "main",
                        "repo_dirty_flag": False,
                        "dirty_files": "",
                        "version": "1.4.4",
                        "open_ephys": [],
                        "ManualWaterVolume": [
                            0,
                            0
                        ],
                        "saving_type_label": "normal saving",
                        "SessionFolder": "C:\\behavior_data\\447-2-B\\730945\\behavior_730945_2024-09-03_15-49-53",
                        "TrainingFolder": "C:\\behavior_data\\447-2-B\\730945\\behavior_730945_2024-09-03_15-49-53\\behavior",
                        "HarpFolder": "C:\\behavior_data\\447-2-B\\730945\\behavior_730945_2024-09-03_15-49-53\\behavior\\raw.harp",
                        "VideoFolder": "C:\\behavior_data\\447-2-B\\730945\\behavior_730945_2024-09-03_15-49-53\\behavior-videos",
                        "PhotometryFolder": "C:\\behavior_data\\447-2-B\\730945\\behavior_730945_2024-09-03_15-49-53\\fib",
                        "MetadataFolder": "C:\\behavior_data\\447-2-B\\730945\\behavior_730945_2024-09-03_15-49-53\\metadata-dir",
                        "SaveFile": "C:\\behavior_data\\447-2-B\\730945\\behavior_730945_2024-09-03_15-49-53\\behavior\\730945_2024-09-03_15-49-53.json",
                        "fiber_photometry_start_time": "",
                        "fiber_photometry_end_time": "",
                        "fiber_mode": "Normal",
                        "session_metadata": {},
                        "generate_session_metadata_success": True,
                        "generate_rig_metadata_success": True,
                        "generate_data_description_success": False,
                        "drop_frames_tag": 0,
                        "trigger_length": 0,
                        "drop_frames_warning_text": "",
                        "frame_num": {}
                        }
                    },
                    "reward_consumed_during_epoch": "372.0",
                    "reward_consumed_unit": "microliter",
                    "trials_total": 493,
                    "trials_finished": 434,
                    "trials_rewarded": 186,
                    "notes": "The duration of go cue is 100ms. The frequency is 7500Hz. Decibel is 76dB. The total reward consumed in the session is 372.0 microliter. The total reward indcluding consumed in the session and supplementary water is 1.0 millimeters."
                    }
                ],
                "mouse_platform_name": "mouse_tube_foraging",
                "active_mouse_platform": False,
                "reward_delivery": None,
                "reward_consumed_total": "372.0",
                "reward_consumed_unit": "microliter",
                "notes": ""
                }
        }
    )
    sample_metadata = json.dumps([[{
    "_id": "d88c355a-f3ea-4f75-879f-9dca358ec5bb",
    "created": "2024-06-20T21:02:37.011333",
    "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/core/metadata.py",
    "external_links": {
        "Code Ocean": [
        "97189da9-88ea-4d85-b1b0-ceefb9299f1a"
        ]
    },
    "last_modified": "2024-09-23T20:30:53.461182",
    "location": "s3://aind-open-data/SmartSPIM_662616_2023-03-06_17-47-13",
    "metadata_status": "Unknown",
    "name": "SmartSPIM_662616_2023-03-06_17-47-13",
    "schema_version": "0.2.7",
    }]])

    quality_control_prompt = f"""
The quality_control schema defines how quality metrics are organized and evaluated for data assets:

- Each data asset has an array of "evaluations"
- Each evaluation contains:
  - modality: The type of data (SPIM, ecephys, behavior, etc.)
  - stage: When quality was assessed (Raw data, Processing, Analysis, Multi-asset)
  - metrics: Array of individual measurements with name, value, and status history
  - status: Overall Pass/Fail/Pending status of the evaluation
Important quality_control query patterns:
1. To query evaluation properties:
   {{"quality_control.evaluations": {{"\\$elemMatch": {{<conditions>}}}}}}

2. To unwind and query individual evaluations:
   [{{"\\$unwind": "$quality_control.evaluations"}}, {{"\\$match": {{"quality_control.evaluations.<field>": <value>}}}}]

3. To query metrics within evaluations:
   [{{"\\$unwind": "$quality_control.evaluations"}}, 
    {{"\\$unwind": "$quality_control.evaluations.metrics"}},
    {{"\\$match": {{"quality_control.evaluations.metrics.name": <metric_name>}}}}]

4. For aggregating QC statistics:
   [{{"\\$unwind": "$quality_control.evaluations"}},
    {{"\\$group": {{"_id": "$quality_control.evaluations.modality.abbreviation", "count": {{"\\$sum": 1}}}}}}]

Example queries:
- Find assets with failed quality control evaluations: 
  {{"quality_control.evaluations.latest_status": "Fail"}}
- Find SPIM data with pending QC: 
  {{"quality_control.evaluations": {{"\\$elemMatch": {{"modality.abbreviation": "SPIM", "latest_status": "Pending"}}}}}}
- Count metrics per evaluation: 
  {{"\\$project": {{"metricCount": {{"\\$size": "$quality_control.evaluations.metrics"}}}}}}
"""


    metadata_prompt = f"""
The following dictionaries are examples of how each major class in the metadata is structured in a sample asset.
This is a sample procedures field: {sample_procedures}. In order to access fields, start with 'procedures.<field>, like procedures.subject_procedures.
This is a sample acquisition field: {sample_acquisition}. In order to access fields, start with 'acquisition.<field>, like acquisition.sample_immersion.
This is a sample instrument field: {sample_instrument}. In order to access fields, start with 'instrument.<field>, like instrument.instrument_id.
This is a sample rig field: {sample_rig}. In order to access fields, start with 'rig.<field>, like rig.rig_id.
This is a sample session field: {sample_session}. In order to access fields, start with 'session.<field>, like session.animal_weight_prior.
This is a sample processing field: {sample_processing}. In order to access fields, start with 'processing.<field>, like processing.analyses.
This is a sample data_description field {sample_data_description}. In order to access fields, start with 'data_description.<field>, like data_description.project_name.
This is a sample subject field {sample_subject}. In order to access fields, start with 'subject.<field>, like subject.project_name.

There are several miscellaneous top level fields which are represented here {sample_metadata}.These can just be accessed by the field name.
"""

    schema_prompt = f"""
You are an expert neuroscientist professor who is proficient at constructing mongodb queries based on a user's query. This is the user's query: {query}
Your task is to teach the next agent how to use the fields in the metadata schema to best construct a python script or mongodb query to best answer the user's query. 
The database you will be working with is a neuroscience metadata database. Follow the instructions below to create queries specific to the type of data found in the database. 
Do not make up fields. It is vital you do not hallucinate.

If the tool call count number {tool_call_count} exceeds 2, do not call tool use, proceed with summarizing what you know to hand off to the next agent.
For simple queries use the following context to construct and execute MongoDB queries. For complex queries, use the schema context for additional information.

  
Key Requirements when creating MongoDB queries:
Always unwind procedures field
Use data_description.modality.name for modality queries
For questions on modalities, always unwind the modalities field.
Use $regex over $elemmatch

Handle duration queries carefully: 
To find the duration of a session, strictly follow the following aggregation stage - 
{{
    $addFields: {{
      session_duration_ms: {{
        $subtract: [
          {{ $dateFromString: {{ dateString: "$session.session_end_time" }} }},
          {{ $dateFromString: {{ dateString: "$session.session_start_time" }} }}
        ]
      }}
    }}
  }}

To find the duration of an acquisition, strictly follow the following aggregation stage - 
{{
    $addFields: {{
      session_duration_ms: {{
        $subtract: [
          {{ $dateFromString: {{ dateString: "$acquisition.session_end_time" }} }},
          {{ $dateFromString: {{ dateString: "$acquisition.session_start_time" }} }}
        ]
      }}
    }}
  }}

Note that the session field is used for physiology based modalities like behaviour, optical physiology etc and acquisition is used for modalities like smartspim or exaspim. If a question is ambiguous or you are unsure which field the data might exist in, use both fields, do not prioritize one over the other. 

If unsure about the name of a field, use regex and the option i, to be flexible with capitalization. For example, {{data_description.project_name: {{ $regex: "patch foraging", $options: 'i' }}}}

Here are the different modality types:
Access them through data_description.modality.name or data_description.modality.abbreviation
1.                                                                                                                                                              
    abbreviation:  "behavior"
2.
    name: "Behavior videos"
    abbreviation: "behavior -videos"
3.           
    name: "Confocal microscopy"
    abbreviation: "confocal"
4.                                                                                                          
    name: "Electromyography"
    abbreviation: "EMG"                                                                    
5.
name: "Extracellular electrophysiology"
 abbreviation:  "ecephys"
 6.                       
    name: "Fiber photometry"                       
    abbreviation: "fib"
7.                                                  
    name: "Fluorescence micro-optical sectioning tomography"
    abbreviation: "fMOST"
8.
    name: "Intracellular electrophysiology"
    abbreviation: "icephys"
9.
    name:"Intrinsic signal imaging"
    abbreviation:"ISI"
10.
    name:"Magnetic resonance imaging"
    abbreviation:  "MRI"
11.

    name:  "Multiplexed error-robust fluorescence in situ hybridization"
    abbreviation: "merfish"
12.
    name: "Planar optical physiology"
    abbreviation: "pophys"

13.
    name: "Scanned line projection imaging"
    abbreviation:  "slap"

14.
    name:  "Selective plane illumination microscopy"
    abbreviation: "SPIM"

Your task is to return any relevant information about how to plan to construct the mongodb query for the next agent, which will execute the query. 
Do not construct mongodb queries, the next agent ill take care of that.

This is the current context we have about the schema: {schema_context}. If it is not sufficient, and you are unable to gather the context you need from the schema above, proceed with tool use. 
If it is sufficient, do not call tool use. Do not make unnecessary tool calls.

Do not overcomplicate your task. If the query can be answerable with the schema context provided above, proceed with that information, do not call tool use.  
Ensure your answer is concise and informative. Communicate ALL relevant information in this prompt to the next agent, even notes on fields that can be used/unused etc. 

Ensure that the fields you determine are best for answering the question actually exist. 
Do not pass along information that's false or non existent. It is crucial you follow this step.

When planning mongodb aggregations do not overcomplicate things. Think of the simplest way you can solve the problem. 
If it too many complex calculations will be done within the aggregation, do not proceed. suggest the simplest version of the aggregation, 
and tell the next agent to use python to continue solving the complex calculations.

When summarizing give all information related to fields that will be helpful in the calculation. 
Spell out the entire nesting structure, so pass on information like "procedures.subject_procedures[].weight_unit", "subject.subject_id".

"""
    

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{schema_prompt}",
                },
                {
                    "type": "text",
                    "text": f"{metadata_prompt}",
                },
                {
                    "type": "text",
                    "text": f"{quality_control_prompt}",
                },
                {
                    "cachePoint": {"type": "default"},
                },
            ],
        },
    ]

    return messages