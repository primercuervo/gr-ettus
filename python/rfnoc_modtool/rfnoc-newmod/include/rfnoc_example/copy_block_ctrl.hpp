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

#ifndef INCLUDED_LIBUHD_RFNOC_copy_block_ctrl_HPP
#define INCLUDED_LIBUHD_RFNOC_copy_block_ctrl_HPP

#include <uhd/rfnoc/source_block_ctrl_base.hpp>
#include <uhd/rfnoc/sink_block_ctrl_base.hpp>

namespace uhd {
    namespace rfnoc {

/*! \brief Block controller for the standard copy RFNoC block.
 *
 * Example RFnoC Controller. Does nothing yet
 */
class UHD_API copy_block_ctrl : public source_block_ctrl_base, public sink_block_ctrl_base
{
public:
    UHD_RFNOC_BLOCK_OBJECT(copy_block_ctrl)

    //! Configure the filter taps.
    //
    // The length of \p taps must correspond the number of taps
    // in this block. If it's shorter, zeros will be padded.
    // If it's longer, throws a uhd::value_error.
    //virtual void set_taps(const std::vector<int> &taps) = 0;

    //! Returns the number of filter taps in this block.
    //virtual size_t get_n_taps() const = 0;
}; /* class copy_block_ctrl*/

}} /* namespace uhd::rfnoc */

#endif /* INCLUDED_LIBUHD_RFNOC_copy_block_ctrl_HPP */
// vim: sw=4 et:
