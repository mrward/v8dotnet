{  
      "includes": [
        "common.gypi"
    ],
   'variables':{  
      'base_dir%':'<(base_dir)',
      'target_arch%':'ia32',
      'build_option%':'release',

   },
   'targets':[  
      {  
         'target_name':'libV8_Net_Proxy',
         'type':'shared_library',
         'toolsets': [ 'target' ],
         'msvs_guid':'5ECEC9E5-8F23-47B6-93E0-C3B328B3BE65',
         'direct_dependent_settings':{  
            'include_dirs':[  
               'Source/V8.NET-Proxy/V8/'
            ],
         },
         'include_dirs':[  
            'Source/V8.NET-Proxy/V8/',
         ],
         'sources':[  
            'Source/V8.NET-Proxy/Exports.cpp',
            'Source/V8.NET-Proxy/FunctionTemplateProxy.cpp',
            'Source/V8.NET-Proxy/HandleProxy.cpp',
            'Source/V8.NET-Proxy/ObjectTemplateProxy.cpp',
            'Source/V8.NET-Proxy/Utilities.cpp',
            'Source/V8.NET-Proxy/V8EngineProxy.cpp',
            'Source/V8.NET-Proxy/ValueProxy.cpp',
         ],
         'conditions':[  
               ['OS=="mac"',
               {  
                  'cflags':[  
                     '-Werror -Wall -std=c++11 -w -fpermissive -fPIC -c',
                  ],
                  'ldflags':[  
                     '-Wall -std=c++11 -shared -fPIC',
                  ],
                  'xcode_settings':{  
                     'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
                     'CLANG_CXX_LIBRARY': 'libc++',
                  },
                  'copies':[  
                     {  
                        'destination':'<(PRODUCT_DIR)/../../',
                        'files':[  
                           'Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/libicui18n.dylib',
                           'Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/libicuuc.dylib',
                           'Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/libv8.dylib',
                        ],
                     }
                  ],
                  'link_settings':{  
                     'libraries':[  
                        '-Wl,-rpath,. -L. -L../',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/obj.target/testing/libgmock.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/obj.target/testing/libgtest.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/obj.target/third_party/icu/libicudata.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/obj.target/tools/gyp/libv8_base.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/obj.target/tools/gyp/libv8_libbase.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/obj.target/tools/gyp/libv8_libplatform.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/obj.target/tools/gyp/libv8_nosnapshot.a',
                        '<(base_dir)/Source/V8.NET-Proxy/V8/out/<(target_arch).<(build_option)/obj.target/tools/gyp/libv8_snapshot.a',
                        '-lpthread -lstdc++ -lv8 -licui18n -licuuc -lglib-2.0 -lrt'
                     ]
                  },
                  'include_dirs':[  
                     '/usr/include/glib-2.0/',
                     '/usr/lib/x86_64-linux-gnu/glib-2.0/include/',
                     '/Library/Frameworks/Mono.framework/Versions/3.10.0/lib/glib-2.0/include/',
                     '/Library/Frameworks/Mono.framework/Versions/3.10.0/include/glib-2.0/',
                  ],
               }],
               ['OS=="win"',
                  {  
                     'defines':[  
                        'WINDOWS_SPECIFIC_DEFINE',
                     ]
                  }
               ]
            ]
      } 
   ]
}