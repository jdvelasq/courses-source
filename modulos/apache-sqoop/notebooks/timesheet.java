// ORM class for table 'timesheet'
// WARNING: This class is AUTO-GENERATED. Modify at your own risk.
//
// Debug information:
// Generated date: Fri May 27 15:38:54 UTC 2022
// For connector: org.apache.sqoop.manager.MySQLManager
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.Writable;
import org.apache.hadoop.mapred.lib.db.DBWritable;
import com.cloudera.sqoop.lib.JdbcWritableBridge;
import com.cloudera.sqoop.lib.DelimiterSet;
import com.cloudera.sqoop.lib.FieldFormatter;
import com.cloudera.sqoop.lib.RecordParser;
import com.cloudera.sqoop.lib.BooleanParser;
import com.cloudera.sqoop.lib.BlobRef;
import com.cloudera.sqoop.lib.ClobRef;
import com.cloudera.sqoop.lib.LargeObjectLoader;
import com.cloudera.sqoop.lib.SqoopRecord;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.sql.Date;
import java.sql.Time;
import java.sql.Timestamp;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class timesheet extends SqoopRecord  implements DBWritable, Writable {
  private final int PROTOCOL_VERSION = 3;
  public int getClassFormatVersion() { return PROTOCOL_VERSION; }
  public static interface FieldSetterCommand {    void setField(Object value);  }  protected ResultSet __cur_result_set;
  private Map<String, FieldSetterCommand> setters = new HashMap<String, FieldSetterCommand>();
  private void init0() {
    setters.put("driverId", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        timesheet.this.driverId = (Integer)value;
      }
    });
    setters.put("week", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        timesheet.this.week = (Integer)value;
      }
    });
    setters.put("hours_logged", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        timesheet.this.hours_logged = (Integer)value;
      }
    });
    setters.put("miles_logged", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        timesheet.this.miles_logged = (Integer)value;
      }
    });
  }
  public timesheet() {
    init0();
  }
  private Integer driverId;
  public Integer get_driverId() {
    return driverId;
  }
  public void set_driverId(Integer driverId) {
    this.driverId = driverId;
  }
  public timesheet with_driverId(Integer driverId) {
    this.driverId = driverId;
    return this;
  }
  private Integer week;
  public Integer get_week() {
    return week;
  }
  public void set_week(Integer week) {
    this.week = week;
  }
  public timesheet with_week(Integer week) {
    this.week = week;
    return this;
  }
  private Integer hours_logged;
  public Integer get_hours_logged() {
    return hours_logged;
  }
  public void set_hours_logged(Integer hours_logged) {
    this.hours_logged = hours_logged;
  }
  public timesheet with_hours_logged(Integer hours_logged) {
    this.hours_logged = hours_logged;
    return this;
  }
  private Integer miles_logged;
  public Integer get_miles_logged() {
    return miles_logged;
  }
  public void set_miles_logged(Integer miles_logged) {
    this.miles_logged = miles_logged;
  }
  public timesheet with_miles_logged(Integer miles_logged) {
    this.miles_logged = miles_logged;
    return this;
  }
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof timesheet)) {
      return false;
    }
    timesheet that = (timesheet) o;
    boolean equal = true;
    equal = equal && (this.driverId == null ? that.driverId == null : this.driverId.equals(that.driverId));
    equal = equal && (this.week == null ? that.week == null : this.week.equals(that.week));
    equal = equal && (this.hours_logged == null ? that.hours_logged == null : this.hours_logged.equals(that.hours_logged));
    equal = equal && (this.miles_logged == null ? that.miles_logged == null : this.miles_logged.equals(that.miles_logged));
    return equal;
  }
  public boolean equals0(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof timesheet)) {
      return false;
    }
    timesheet that = (timesheet) o;
    boolean equal = true;
    equal = equal && (this.driverId == null ? that.driverId == null : this.driverId.equals(that.driverId));
    equal = equal && (this.week == null ? that.week == null : this.week.equals(that.week));
    equal = equal && (this.hours_logged == null ? that.hours_logged == null : this.hours_logged.equals(that.hours_logged));
    equal = equal && (this.miles_logged == null ? that.miles_logged == null : this.miles_logged.equals(that.miles_logged));
    return equal;
  }
  public void readFields(ResultSet __dbResults) throws SQLException {
    this.__cur_result_set = __dbResults;
    this.driverId = JdbcWritableBridge.readInteger(1, __dbResults);
    this.week = JdbcWritableBridge.readInteger(2, __dbResults);
    this.hours_logged = JdbcWritableBridge.readInteger(3, __dbResults);
    this.miles_logged = JdbcWritableBridge.readInteger(4, __dbResults);
  }
  public void readFields0(ResultSet __dbResults) throws SQLException {
    this.driverId = JdbcWritableBridge.readInteger(1, __dbResults);
    this.week = JdbcWritableBridge.readInteger(2, __dbResults);
    this.hours_logged = JdbcWritableBridge.readInteger(3, __dbResults);
    this.miles_logged = JdbcWritableBridge.readInteger(4, __dbResults);
  }
  public void loadLargeObjects(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void loadLargeObjects0(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void write(PreparedStatement __dbStmt) throws SQLException {
    write(__dbStmt, 0);
  }

  public int write(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeInteger(driverId, 1 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeInteger(week, 2 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeInteger(hours_logged, 3 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeInteger(miles_logged, 4 + __off, 4, __dbStmt);
    return 4;
  }
  public void write0(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeInteger(driverId, 1 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeInteger(week, 2 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeInteger(hours_logged, 3 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeInteger(miles_logged, 4 + __off, 4, __dbStmt);
  }
  public void readFields(DataInput __dataIn) throws IOException {
this.readFields0(__dataIn);  }
  public void readFields0(DataInput __dataIn) throws IOException {
    if (__dataIn.readBoolean()) { 
        this.driverId = null;
    } else {
    this.driverId = Integer.valueOf(__dataIn.readInt());
    }
    if (__dataIn.readBoolean()) { 
        this.week = null;
    } else {
    this.week = Integer.valueOf(__dataIn.readInt());
    }
    if (__dataIn.readBoolean()) { 
        this.hours_logged = null;
    } else {
    this.hours_logged = Integer.valueOf(__dataIn.readInt());
    }
    if (__dataIn.readBoolean()) { 
        this.miles_logged = null;
    } else {
    this.miles_logged = Integer.valueOf(__dataIn.readInt());
    }
  }
  public void write(DataOutput __dataOut) throws IOException {
    if (null == this.driverId) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.driverId);
    }
    if (null == this.week) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.week);
    }
    if (null == this.hours_logged) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.hours_logged);
    }
    if (null == this.miles_logged) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.miles_logged);
    }
  }
  public void write0(DataOutput __dataOut) throws IOException {
    if (null == this.driverId) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.driverId);
    }
    if (null == this.week) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.week);
    }
    if (null == this.hours_logged) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.hours_logged);
    }
    if (null == this.miles_logged) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.miles_logged);
    }
  }
  private static final DelimiterSet __outputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  public String toString() {
    return toString(__outputDelimiters, true);
  }
  public String toString(DelimiterSet delimiters) {
    return toString(delimiters, true);
  }
  public String toString(boolean useRecordDelim) {
    return toString(__outputDelimiters, useRecordDelim);
  }
  public String toString(DelimiterSet delimiters, boolean useRecordDelim) {
    StringBuilder __sb = new StringBuilder();
    char fieldDelim = delimiters.getFieldsTerminatedBy();
    __sb.append(FieldFormatter.escapeAndEnclose(driverId==null?"null":"" + driverId, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(week==null?"null":"" + week, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(hours_logged==null?"null":"" + hours_logged, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(miles_logged==null?"null":"" + miles_logged, delimiters));
    if (useRecordDelim) {
      __sb.append(delimiters.getLinesTerminatedBy());
    }
    return __sb.toString();
  }
  public void toString0(DelimiterSet delimiters, StringBuilder __sb, char fieldDelim) {
    __sb.append(FieldFormatter.escapeAndEnclose(driverId==null?"null":"" + driverId, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(week==null?"null":"" + week, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(hours_logged==null?"null":"" + hours_logged, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(miles_logged==null?"null":"" + miles_logged, delimiters));
  }
  private static final DelimiterSet __inputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  private RecordParser __parser;
  public void parse(Text __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharSequence __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(byte [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(char [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(ByteBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  private void __loadFromFields(List<String> fields) {
    Iterator<String> __it = fields.listIterator();
    String __cur_str = null;
    try {
    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.driverId = null; } else {
      this.driverId = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.week = null; } else {
      this.week = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.hours_logged = null; } else {
      this.hours_logged = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.miles_logged = null; } else {
      this.miles_logged = Integer.valueOf(__cur_str);
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  private void __loadFromFields0(Iterator<String> __it) {
    String __cur_str = null;
    try {
    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.driverId = null; } else {
      this.driverId = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.week = null; } else {
      this.week = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.hours_logged = null; } else {
      this.hours_logged = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.miles_logged = null; } else {
      this.miles_logged = Integer.valueOf(__cur_str);
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  public Object clone() throws CloneNotSupportedException {
    timesheet o = (timesheet) super.clone();
    return o;
  }

  public void clone0(timesheet o) throws CloneNotSupportedException {
  }

  public Map<String, Object> getFieldMap() {
    Map<String, Object> __sqoop$field_map = new HashMap<String, Object>();
    __sqoop$field_map.put("driverId", this.driverId);
    __sqoop$field_map.put("week", this.week);
    __sqoop$field_map.put("hours_logged", this.hours_logged);
    __sqoop$field_map.put("miles_logged", this.miles_logged);
    return __sqoop$field_map;
  }

  public void getFieldMap0(Map<String, Object> __sqoop$field_map) {
    __sqoop$field_map.put("driverId", this.driverId);
    __sqoop$field_map.put("week", this.week);
    __sqoop$field_map.put("hours_logged", this.hours_logged);
    __sqoop$field_map.put("miles_logged", this.miles_logged);
  }

  public void setField(String __fieldName, Object __fieldVal) {
    if (!setters.containsKey(__fieldName)) {
      throw new RuntimeException("No such field:"+__fieldName);
    }
    setters.get(__fieldName).setField(__fieldVal);
  }

}
