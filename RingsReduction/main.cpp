#include <iostream>

#include "Data3D.h"
#include "GLViwerCore.h"
#include "RingsReduction.h"

#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;


int main()
{

    // laoding data
    Data3D<short> im_short;
    bool flag = im_short.load( "../temp/vessel3d.data", Vec3i(585, 525, 10), true, true );
    if( !flag ) return 0;

    // save the center slice
    {
        Mat src_norm;
        cv::normalize(im_short.getMat( im_short.SZ()/2 ), src_norm, 0, 255, NORM_MINMAX, CV_8UC1);
        cv::imwrite("output/before_redution.png", src_norm );
    }

    // compute the minimum value and maximum value in the centre slice
    double minVal = 0, maxVal = 0;
    cv::minMaxLoc( im_short.getMat( im_short.SZ()/2 ), &minVal, &maxVal );

    // rings resuction - unname method
    if( 1 )
    {
        Data3D<short> im_rduct;
        RR::unname_method( im_short, im_rduct );

        if( 0 )
        {
            // save the centre slice of result
            Mat dst_norm = im_rduct.getMat( im_rduct.SZ()/2 );
            // change the data type from whatever dataype it is to float for computation
            dst_norm.convertTo(dst_norm, CV_32F);
            // normalize the data range from whatever it is to [0, 255];
            dst_norm = 255.0f * (  dst_norm - minVal ) / (maxVal - minVal);
            // convert back to CV_8U for visualizaiton
            dst_norm.convertTo(dst_norm, CV_8U);
            // save file
            cv::imwrite("output/after_reduction.png", dst_norm );
        }
    }

//    if( false )
//    {
//        Data3D<short> im_rduct;
//        RR::mm_filter( im_short, im_rduct );
//
//        // save the centre slice of result
//        Mat dst_norm = im_rduct.getMat( im_rduct.SZ()/2 );
//        // change the data type from whatever dataype it is to float for computation
//        dst_norm.convertTo(dst_norm, CV_32F);
//        // normalize the data range from whatever it is to [0, 255];
//        dst_norm = 255.0f * (  dst_norm - minVal ) / (maxVal - minVal);
//        // convert back to CV_8U for visualizaiton
//        dst_norm.convertTo(dst_norm, CV_8U);
//        // save file
//        cv::imwrite("output/after_reduction_mmfilter.png", dst_norm );
//    }
//

    if( 1 )
    {
        Data3D<short> im_rduct;

        RR::polar_avg_diff( im_short, im_rduct );

        if( 1 )
        {
            // save the centre slice of result
            Mat dst_norm = im_rduct.getMat( im_rduct.SZ()/2 );
            // change the data type from whatever dataype it is to float for computation
            dst_norm.convertTo(dst_norm, CV_32F);
            // normalize the data range from whatever it is to [0, 255];
            dst_norm = 255.0f * (  dst_norm - minVal ) / (maxVal - minVal);
            // convert back to CV_8U for visualizaiton
            dst_norm.convertTo(dst_norm, CV_8U);
            // save file
            cv::imwrite( "output/polar_avg_diff.png", dst_norm );
        }
    }

    return 0;
}

