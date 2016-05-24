//
// Copyright 2014 Ettus Research LLC
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
//

#include <rfnoc_example/copy_block_ctrl.hpp>
#include <uhd/convert.hpp>
#include <uhd/utils/msg.hpp>

using namespace uhd::rfnoc;

class copy_block_ctrl_impl : public copy_block_ctrl
{
public:
    /*
    static const boost::uint32_t RB_NUM_TAPS            = 0;
    static const boost::uint32_t AXIS_FIR_RELOAD       = AXIS_CONFIG_BUS+0; // 2*0+0
    static const boost::uint32_t AXIS_FIR_RELOAD_TLAST = AXIS_CONFIG_BUS+1; // 2*0+1
    static const boost::uint32_t AXIS_FIR_CONFIG       = AXIS_CONFIG_BUS+2; // 2*1+0
    static const boost::uint32_t AXIS_FIR_CONFIG_TLAST = AXIS_CONFIG_BUS+3; // 2*1+1
*/
    UHD_RFNOC_BLOCK_CONSTRUCTOR(copy_block_ctrl)
      //  _item_type("sc16") // We only support sc16 in this block
    {
//        UHD_MSG(status) << "copy_block::copy_block() max_len ==" << _max_len << std::endl;
 //       UHD_ASSERT_THROW(_max_len);

    }


private:
  //  const std::string _item_type;
   // size_t _max_len;
};

UHD_RFNOC_BLOCK_REGISTER(copy_block_ctrl, "Copy");
